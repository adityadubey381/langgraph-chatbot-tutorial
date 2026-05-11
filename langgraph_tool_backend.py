# backedn.py

from langgraph.graph import StateGraph, START, END
from typing import Annotated, TypedDict
from langchain_core.messages import HumanMessage, BaseMessage
from langchain_openai import ChatOpenAI
from langgraph.graph.message import add_messages
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.prebuilt import tools_condition, ToolNode
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
from dotenv import load_dotenv
import sqlite3
import requests

load_dotenv()

#----------------------------------
# 1. LLM
#----------------------------------

llm = ChatOpenAI()

#----------------------------------
# 2. Tools
#----------------------------------

search_tool = DuckDuckGoSearchRun()

@tool
def calculator(first_num: float, second_num: float, operation: str) -> dict:
    """
    Perform a basic arithmetic operation on two number
    Supported operations: add, sub, mul, div
    """
    try:
        if operation == 'add':
            result = first_num + second_num
        elif operation == 'sub':
            result = first_num - second_num
        elif operation == 'mul':
            result = first_num * second_num
        elif operation == 'div':
            if second_num == 0:
                return {'error':'Division by zero is not allowed'}
            result = first_num / second_num
        else:
            return {"error": f"Unsupported operation '{operation}'"}
        
        return{"first_num": first_num, "second_num": second_num, "result": result}

    except Exception as e:
        return {"error": str(e)}
    

@tool
def get_stock_price(symbol: str) -> dict:
    """
    Fetch latest stock Price for a given symbol (e.g. 'APPL', 'TSLA')
    using Alpha Vantage API key in the URL.
    """
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&interval=5min&apikey=XNGD1XY426LWZC9G'
    r = requests.get(url)
    return r.json()



tools = [search_tool, calculator, get_stock_price]
llm_with_tools = llm.bind_tools(tools)



# -------------------
# 3. State
# -------------------
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

# -------------------
# 4. Nodes
# -------------------
def chat_node(state: ChatState):
    """LLM node that may answer or request a tool call."""
    messages= state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

tool_node = ToolNode(tools)

#----------------------------------
# 5. Check pointer
#----------------------------------
conn = sqlite3.connect(database='chatbot.db', check_same_thread=False)
checkpointer = SqliteSaver(conn=conn)


#----------------------------------
# 6. Graph
#----------------------------------
graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_node("tools", tool_node)

graph.add_edge(START, "chat_node")
graph.add_conditional_edges("chat_node", tools_condition)
graph.add_edge('tools', 'chat_node')

chatbot = graph.compile(checkpointer=checkpointer)

#----------------------------------
# 7. Helper
#----------------------------------

def retrieve_all_threads():
    all_therads = set()
    for checkpoint in checkpointer.list(None):
        all_therads.add(checkpoint.config["configurable"]["thread_id"])
    return list(all_therads)
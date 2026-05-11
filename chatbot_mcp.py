from langgraph.graph import StateGraph,START
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchResults
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.tools import tool
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()

llm = ChatOpenAI()

# MCP client for local FastMCP server
client = MultiServerMCPClient(
    {
        #"arith": {
        #    "transport": "stdio",
        #    "command": "python3",
        #    "args":["Users/nitish/Desktop/mcp-math-server/main.py"]
        #},
        "expences":{
            "transport": "streamable_http", # if this fails, try "sse"
            "url": "https://splendid-gold-dingo.fastmcp.app/mcp"
        }
    }
)
    

# state
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

# defining graph and nodes
async def build_graph():

    tools = await client.get_tools()
    
    llm_with_tools = llm.bind_tools(tools)

    # nodes
    async def chat_node(state: ChatState):
    
        messages= state["messages"]
        response = await llm_with_tools.ainvoke(messages)
        return {"messages": [response]}
    

    tool_node = ToolNode(tools)

    # defining graph and nodes
    graph = StateGraph(ChatState)

    graph.add_node("chat_node", chat_node)
    graph.add_node("tools", tool_node)

    # defining graph connections
    graph.add_edge(START, "chat_node")
    graph.add_conditional_edges("chat_node", tools_condition)
    graph.add_edge('tools', 'chat_node')

    chatbot = graph.compile()

    return chatbot

async def main():

    chatbot = await build_graph()

    # running the graph
    result = await chatbot.ainvoke({'messages':[HumanMessage(content='Give me all the expenses of for the month of Nov. ')]})
    
    print(result['messages'][-1].content)

if __name__ == '__main__':
    asyncio.run(main())
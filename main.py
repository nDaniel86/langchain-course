from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()


# @tool
# def search(query: str) -> str:
#     """
#     Tool that searches over internet
#     Args:
#         query (str): search query
#     Returns:
#         str: search result
#     :param query:
#     :return:
#     """
#     print(f"Searching {query}")
#     # return "Tokyo weather is sunny"
#     return tavily.search(query=query)

llm = ChatOpenAI(model="gpt-5-nano")

tools = [TavilySearch()]

agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello World")
    result = agent.invoke({"messages": HumanMessage(content="What is the weather in Tokyo?")})

    print(result)


if __name__ == "__main__":
    main()
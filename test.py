from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from agno.models.groq import Groq

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=Groq(id="qwen-qwq-32b"),
    tools=[DuckDuckGoTools()],
    instructions="Always include sources",
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Groq(id="qwen-qwq-32b"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,stock_fundamentals=True,company_info=True,technical_indicators =True, historical_prices =True)],
    instructions="Use tables to display data",
    show_tool_calls=True,
    markdown=True,
)


agent_team = Agent(
    team=[web_agent, finance_agent],
    model=Groq(id="qwen-qwq-32b"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response("Analyze the market outlook and financial performance of TESLA stock and APPLE stock. Tell me which to hold and which to sell ", stream=True)
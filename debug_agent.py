from crewai import Agent, Task, Crew
from crewai.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

@tool("Search Catalog")
def search_catalog_tool(requirement: str):
    """
    Search the product catalog for the best matching SKU based on requirements.
    Returns the top matching SKU details as a JSON string.
    """
    return "SKU FOUND: TEST-101"

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.2,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

agent = Agent(
    role="Tester",
    goal="Test tool",
    backstory="Tester",
    tools=[search_catalog_tool],
    llm=llm,
    verbose=True
)

task = Task(
    description="Find a product matching 'heat resistant'. Use the Search Catalog tool.",
    expected_output="Result",
    agent=agent
)

crew = Crew(agents=[agent], tasks=[task])
crew.kickoff()

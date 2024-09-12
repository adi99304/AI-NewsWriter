from crewai import Agent
from dotenv import load_dotenv
import os
load_dotenv()
from tools import tool_search
# Call the gemini model 
from langchain_google_genai import ChatGoogleGenerativeAI
# Call the gemini models
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,  # details of what is getting executed
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Researcher agent
researcher = Agent(
    role="senior researcher",
    goal="uncover groundbreaking technologies in topic {topic}",
    memory=True,
    backstory="Driven by curiosity, you are at the forefront of innovation, eager to change the world.",
    llm=llm,
    allow_delegation=True,
)

# News writer agent
news_writer = Agent(
    role="senior writer",
    goal="writing compelling tech stories about the topic {topic}",
    memory=True,
    backstory="With a flair for simplifying topics you are fond of, you write something that is easy to understand.",
    llm=llm,
    allow_delegation=True,
)

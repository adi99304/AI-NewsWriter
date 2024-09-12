from crewai import Task
from agents import researcher, news_writer
from tools import tool_search
research_task = Task(
    description="Use Serper to search for news about the topic {topic}",
    agent=researcher,
    expected_output="List of news stories",
    tools=[tool_search],
)

writer_task = Task(
    description="Use Serper to search for the latest news, then generate insightful tech news stories about it.",
    agent=news_writer,
    expected_output="A well-written tech news article",
    tools=[tool_search],
)


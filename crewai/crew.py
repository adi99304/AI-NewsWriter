from crewai import Crew,Process
from tasks import research_task,writer_task
from agents import researcher,news_writer
crew = Crew(
    tasks=[
        research_task,
        writer_task,
    ],
    agents=[
    researcher,
        news_writer,
    ],
    
    process=Process.sequential,
    verbose=True,
)
#starting the task execution process with enhanced feed back
result = crew.kickoff(inputs={
    'topic': 'cricket in india'
})
print(result)
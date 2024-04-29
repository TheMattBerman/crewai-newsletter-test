import os 
import datetime
from crewai import Crew, Process
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from agents import AINewsLetterAgents
from tasks import AINewsLetterTasks
from file_io import save_markdown

#from dotenv import load_dotenv
#load_dotenv()

# Initialize the agents and tasks
agents = AINewsLetterAgents()
tasks = AINewsLetterTasks()

# Initialize the OpenAI GPT-4 language model
OpenAIGPT4 = ChatOpenAI(
    model="gpt-4"
)


# Instantiate the agents
editor = agents.editor_agent()
news_fetcher = agents.news_fetcher_agent()
news_analyzer = agents.news_analyzer_agent()
newsletter_compiler = agents.newsletter_compiler_agent()

# Instantiate the tasks
fetch_news_task = tasks.fetch_news_task(news_fetcher)
analyze_news_task = tasks.analyze_news_task(news_analyzer, [fetch_news_task])
compile_newsletter_task = tasks.compile_newsletter_task(
    newsletter_compiler, [analyze_news_task], save_markdown)

# Form the crew
crew = Crew(
    agents=[editor, news_fetcher, news_analyzer, newsletter_compiler],
    tasks=[fetch_news_task, analyze_news_task, compile_newsletter_task],
    process=Process.hierarchical,
    manager_llm=OpenAIGPT4,
    verbose=2
)

# Kick off the crew's work
results = crew.kickoff()

# Print the results
print("Crew Work Results:")
print(results)

# Save the results to a markdown file
# Ensure the 'results' directory exists
folder_name = "results"
os.makedirs(folder_name, exist_ok=True)

# Get the current date and time
now = datetime.datetime.now()

# Format the date and time as a string 'YYYY-MM-DD-HHMMSS'
formatted_date_time = now.strftime("%Y-%m-%d-%H%M%S")

# Create a file name with the current date and time
file_name = f"{folder_name}/{formatted_date_time}.md"

# Save results to the file
with open(file_name, 'w') as file:
    file.write("# Crew Work Results\n")
    file.write(str(results) + "\n")

print(f"Results saved in file named {file_name}")

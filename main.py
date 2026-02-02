import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
from my_tools import GmailTool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise RuntimeError("API_KEY not set in .env")


my_llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=API_KEY,
    temperature=0.7,
)


career_agent = Agent(
    role="Job Application Assistant",
    goal="Identify if I have received any interview invites or important job updates or any new job postings.",
    backstory="You are an expert career assistant. You are helping a student find a job. You are very careful and never miss an interview invitation or new job post. You only report on actual job-related emails, ignoring generic newsletters.",
    tools=[GmailTool.fetch_job_emails],
    llm=my_llm,
    verbose=True,  # This lets you see the agent "thinking" in the terminal
)

check_emails_task = Task(
    description="Review all unread emails from todayfor mentions of 'interview' or 'job application' or any important job related updates, including application status changes or interview invites or new job postings or openings. If you find any, summarize the company name, the role, and whether I need to take action (like scheduling an interview).If no relevant emails are found, state that the inbox is clear for today.",
    expected_output="A clear, bulleted summary of job updates and urgent actions. withe name of company, role, and next steps if any including which company/organisation sent the email.",
    agent=career_agent,
)

job_hunt_crew = Crew(
    agents=[career_agent],
    tasks=[check_emails_task],
    process="sequential",
)

# Run the process
print("Starting the Job Search Crew... ")
result = job_hunt_crew.kickoff()


print("\n--- FINAL REPORT ---")
print(result)

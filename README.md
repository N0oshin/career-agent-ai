# Career Agent AI
Career Agent AI is an intelligent system built with CrewAI and Google Gemini that automates the tedious task of monitoring job applications. 
Instead of manual inbox skimming, this agent "reads" your Gmail, identifies interview invites and application status changes, and provides a concise daily report.

## Key Features
1. Agentic Reasoning: Uses LLM-based agents to distinguish between actual job updates and generic recruitment newsletters.

2.  API Integration: Securely connects to your inbox to fetch real-time data.

3. Daily Briefing: Automatically filters for emails received today to keep your focus on urgent tasks.

4. Zero Noise Filtering: Built-in logic to ignore social notifications and marketing clutter.

## Tech Stack
- Orchestration: CrewAI

- Brain: Google Gemini 2.5 Flash

- Framework: LangChain

- API: Google Gmail API v1

## Project Structure

├── main.py            
├── my_tools.py       
├── auth_test.py        
├── credentials.json  
├── token.json  
└──.env

## ⚙️ Installation & Setup

##### 1. Clone the Repository
##### 2. Install Dependencies
- _pip install crewai langchain-google-genai google-auth-oauthlib google-api-python-client_
##### 3. Google Cloud Setup
- Enable Gmail API in your Google Cloud Console
- Download credentials.json and place it in the project root directory
##### 4. Authenticate Gmail Access
- Run the auth_test.py file to generate token.json
##### 5. Set Environment Variables
- Create a .env file in the project root and add your Gemini API key




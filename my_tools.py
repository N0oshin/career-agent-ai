from crewai.tools import tool
from auth_test import authenticate_gmail
from datetime import date


class GmailTool:
    @tool(
        "fetch_job_emails"
    )  # "@tool" tells CrewAI: "The function below isn't just a regular Python function; it’s a tool that an AI Agent can use."
    def fetch_job_emails(query: str):
        """
        Search for unread emails in Gmail.
        Input should be a search query like 'is:unread application'
        or 'is:unread interview'.
        """
        service = authenticate_gmail()

        today = date.today().strftime("%Y/%m/%d")
        enhanced_query = f"{query} after:{today}"
        # Search for the emails
        results = (
            service.users().messages().list(userId="me", q=enhanced_query).execute()
        )
        messages = results.get("messages", [])

        if not messages:
            return f"No job emails found for today ({today})."

        # Grab the content of the emails
        output = []
        for msg in messages:
            txt = service.users().messages().get(userId="me", id=msg["id"]).execute()
            headers = txt.get("payload", {}).get("headers", [])
            subject = next(
                (h["value"] for h in headers if h["name"] == "Subject"), "No Subject"
            )
            snippet = txt.get("snippet", "No content snippet available.")
            output.append(f"Subject: {subject}\nContent: {snippet}\n---")

        print("Subjects and snippets of the unread emails:")
        for item in output:
            print(item)

        return "\n".join(output)

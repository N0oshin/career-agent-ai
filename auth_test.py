import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# The 'Scope'
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def authenticate_gmail():
    creds = None
    # token.json stores  access tokens.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If there are no valid credentials, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # If there's no session at all, it looks for that credentials.json downloaded from Google Cloud. It starts a "local server" to let you click "Allow."
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)


if __name__ == "__main__":
    service = authenticate_gmail()
    print("Successfully connected to Gmail!")

    # Let's test it by listing your labels (Inbox, Sent, etc.)
    results = service.users().labels().list(userId="me").execute()
    labels = results.get("labels", [])
    print(f"Found {len(labels)} labels in your account.")

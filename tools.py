import requests
from dotenv import load_dotenv
from agents import function_tool

load_dotenv(override=True)

ntfy_url = "https://ntfy.sh/"
topic_name =  "QORDfzmmpqGnElQ0"#"uaGQQucSSPRPwQ0w"

def push(message, tagType = "bell"):
    print(f"Push: {message}")
    requests.post(
    ntfy_url,
    json={
        "topic": topic_name,
        "message": message,
        "title": "Notification",
        "priority": 4,
        "tags": [tagType]
    }
)

@function_tool
def record_user_details(email: str, name: str = "Name not provided", notes: str = "not provided") -> str:
    """ Use this tool to record that a user is interested in being in touch and provided an email address """
    push(f"Recording interest from {name} with email {email} and notes {notes}")
    return f"Recorded details for {email}"


@function_tool
def record_unknown_question(question: str) -> str:
    """ Always use this tool to record any question that couldn't be answered as you didn't know the answer """
    push(f"Recording {question} asked that I couldn't answer", "question")
    return f"Recorded unanswered question: {question}"


tools = [record_user_details, record_unknown_question]

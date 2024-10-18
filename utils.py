import os
from dotenv import load_dotenv
from datetime import datetime
from serpapi import GoogleSearch
import json

load_dotenv()

def get_flight_prices(departure_id, arrival_id, outbound_date, return_date=None, type="1"):
    params = {
        "api_key": os.getenv("SERP_API_KEY"),
        "engine": "google_flights",
        "hl": "en",
        "gl": "us",
        "type": type,
        "departure_id": departure_id,
        "arrival_id": arrival_id,
        "outbound_date": outbound_date,
        "return_date": return_date,
        "currency": "INR"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return results

def search(Search_input):
    params = {
    "api_key": os.getenv("SERP_API_KEY"),
    "engine": "google",
    "q": Search_input,
    "google_domain": "google.com",
    "hl": "en"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    results = results.get("answer_box").get("answer") if results.get("answer_box") else results.get("related_questions")
    return results


def get_current_date_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def pretty_print_messages(messages) -> None:
    for message in messages:
        if message["role"] != "assistant":
            continue

        print(f"\033[94m{message['sender']}\033[0m:", end=" ")

        if message["content"]:
            print(message["content"])

        tool_calls = message.get("tool_calls") or []
        if len(tool_calls) > 1:
            print()
        for tool_call in tool_calls:
            f = tool_call["function"]
            name, args = f["name"], f["arguments"]
            arg_str = json.dumps(json.loads(args)).replace(":", "=")
            print(f"\033[95m{name}\033[0m({arg_str[1:-1]})")


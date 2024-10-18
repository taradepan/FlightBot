from swarm import Swarm, Agent
import json
from utils import get_flight_prices, search, get_current_date_time, pretty_print_messages
client = Swarm()

agent = Agent(
    name="Agent",
    instructions="""Your task is to check if you got the correct response for the user query.
    In case you don't know the departure_id or arrival_id, you can search for the Airport IATA code. 
    Search for the cheapest flight prices based on the user query and return the results. Check the current date and time (if Needed).
    If user has any more queries, answer them.
    for get_flight_prices, type can be 1, 2, 3.
    1 - Round trip (default)
    2 - One way
    3 - Multi-city
    """,
    functions=[get_flight_prices, search, get_current_date_time],
)

messages = []
while True:
    user_input = input("\033[90mUser\033[0m: ")
    messages.append({"role": "user", "content": user_input})

    response = client.run(
        agent=agent,
        messages=messages,
    )

    pretty_print_messages(response.messages)

    messages.extend(response.messages)
    agent = response.agent
    print("Agent: ", response.agent)

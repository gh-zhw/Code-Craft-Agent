from dotenv import load_dotenv, find_dotenv

from agent import Agent
from agent_tools import *


if __name__ == "__main__":

    load_dotenv(find_dotenv())

    deepseek_chat_model = "deepseek:deepseek-chat"

    agent = Agent(model=deepseek_chat_model)
    agent.add_tool([create_file, write_file, read_file, append_file, exec_shell_command])

    messages = [
        {
            "role": "system",
            "content": "You are CodeCraftAgent, an AI agent that writes and executes code to accomplish any task the user gives you."
        }
    ]

    while True:
        user_resquest = input("\033[91m[User]\033[0m\n>> ")
        messages.append({
            "role": "user",
            "content": user_resquest
        })
        resp = agent.call(messages)
        print("\033[92m[CodeCraftAgent]\033[0m\n>> ", resp)


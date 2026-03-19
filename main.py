from platform import system
from dotenv import load_dotenv, find_dotenv

from agent import Agent
from agent_tools import *


def get_system_prompt(prompt_file="./system_prompt_template.md"):
    os_env = system().lower()  # "linux", "windows", "darwin"

    with open(prompt_file, "r", encoding="utf-8") as f:
        template = f.read()

    filled_prompt = template.replace("{operating_system_env}", os_env)
    return filled_prompt


if __name__ == "__main__":

    # load LLM API keys from .env file
    load_dotenv(find_dotenv())

    deepseek_chat_model = "deepseek:deepseek-chat"

    agent = Agent(model=deepseek_chat_model)
    agent.add_tool([create_file, write_file, read_file, append_file, exec_shell_command])

    messages = [
        {
            "role": "system",
            "content": get_system_prompt()
        }
    ]

    while True:
        user_resquest = input("\033[91m[User]\033[0m\n>> ")
        messages.append({
            "role": "user",
            "content": user_resquest
        })
        resp = agent.call(messages, max_turns=10)
        print("\033[92m[CodeCraftAgent]\033[0m\n>> ", resp)


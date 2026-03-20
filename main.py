from platform import system
from argparse import ArgumentParser
from dotenv import load_dotenv, find_dotenv

from agent import Agent
from agent_tools import *


# load LLM API keys from .env file
load_dotenv(find_dotenv())


def get_system_prompt(prompt_file="./system_prompt_template.md"):
    os_env = system().lower()  # "linux", "windows"

    with open(prompt_file, "r", encoding="utf-8") as f:
        template = f.read()

    filled_prompt = template.replace("{operating_system_env}", os_env)
    return filled_prompt


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument('--auto', action="store_true",
                        help='Enable automaticly executing shell commands without confirmation.')
    args = parser.parse_args()

    deepseek_chat_model = "deepseek:deepseek-chat"

    agent = Agent(model=deepseek_chat_model)
    agent.add_tool([create_file, write_file, read_file, append_file])
    if args.auto:
        agent.add_tool(exec_shell_command_no_confirm)
    else:
        agent.add_tool(exec_shell_command_with_confirm)

    messages = [
        {
            "role": "system",
            "content": get_system_prompt()
        }
    ]

    while True:
        user_resquest = input("\033[91m[User]\033[0m\n: ")
        messages.append({
            "role": "user",
            "content": user_resquest
        })
        resp = agent.call(messages, max_turns=20)
        print("\033[92m[CodeCraftAgent]\033[0m\n: ", resp)


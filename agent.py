import aisuite as ai
from typing import List


client = ai.Client()

class Agent:
    def __init__(self, model : str):
        self.model = model
        self.tools = []

    def set_model(self, model : str):
        '''Set the model for the agent.'''
        self.model = model

    def add_tool(self, tool : callable | List[callable]):
        '''Add a tool or a list of tools to the agent.'''
        if isinstance(tool, list):
            self.tools.extend(tool)
        else:
            self.tools.append(tool)
    
    def call(self, messages : List[dict], max_turns=5):
        '''Call the agent with the given messages'''
        response = client.chat.completions.create(
            model=self.model, 
            messages=messages, 
            tools=self.tools, 
            max_turns=max_turns
        )
        message = response.choices[0].message
        # Append the agent's message to the conversation
        messages.append(message)
        return message.content

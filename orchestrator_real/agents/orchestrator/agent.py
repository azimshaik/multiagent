import logging
import os
from typing import List

from google.adk import Agent
from google.adk.model import Model
from a2a.client import A2AClient
from a2a.resolver import A2ACardResolver

# Configure logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

class OrchestratorAgent:
    def __init__(self):
        self.client = A2AClient()
        self.remote_agents = {}
        
        # Initialize ADK Agent
        self.agent = Agent(
            name="orchestrator",
            model=Model("gemini-1.5-pro"), # Using a real model name
            instruction="You are an Orchestrator. Your goal is to manage deployments and testing by delegating to specialized agents.",
            tools=[self.send_message]
        )

    def send_message(self, agent_name: str, action: str, **kwargs):
        """
        Tool exposed to the LLM to send messages to other agents.
        """
        log.info(f"Delegating task '{action}' to agent '{agent_name}'")
        
        # In a real scenario, we would resolve the address from a registry
        # For this demo, we assume local ports or known addresses
        agent_address = self.remote_agents.get(agent_name)
        if not agent_address:
            return f"Error: Agent {agent_name} not found."

        try:
            response = self.client.send_task(
                target=agent_address,
                task_name=action,
                payload=kwargs
            )
            return response
        except Exception as e:
            return f"Error communicating with {agent_name}: {str(e)}"

    def register_agent(self, name: str, address: str):
        """
        Manually register an agent for the demo.
        """
        self.remote_agents[name] = address
        log.info(f"Registered agent '{name}' at {address}")

    def run(self, user_input: str):
        response = self.agent.run(user_input)
        print(f"Orchestrator Response: {response.text}")

if __name__ == "__main__":
    # Example usage
    orchestrator = OrchestratorAgent()
    orchestrator.register_agent("devops", "http://localhost:8001")
    orchestrator.register_agent("qa", "http://localhost:8002")
    
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break
        orchestrator.run(user_input)

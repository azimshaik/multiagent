import logging
from google.adk import Agent, Tool
from a2a.server import A2AServer

logging.basicConfig(level=logging.INFO)

def build_image(repo_name: str):
    """Builds a Docker image for the repository."""
    print(f"[DevOps] Building image for {repo_name}...")
    return "Image built successfully: v1.0.0"

def deploy_service(service_name: str, image: str):
    """Deploys a service to Cloud Run."""
    print(f"[DevOps] Deploying {service_name} with image {image}...")
    return "Deployment successful."

class DevOpsAgent:
    def __init__(self):
        self.agent = Agent(
            name="devops",
            instruction="You are a DevOps engineer. You handle building and deploying applications.",
            tools=[build_image, deploy_service]
        )
        self.server = A2AServer(self.agent, port=8001)

    def start(self):
        print("Starting DevOps Agent on port 8001...")
        self.server.run()

if __name__ == "__main__":
    DevOpsAgent().start()

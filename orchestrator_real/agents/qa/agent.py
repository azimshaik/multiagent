import logging
from google.adk import Agent
from a2a.server import A2AServer

logging.basicConfig(level=logging.INFO)

def run_tests(suite: str):
    """Runs the specified test suite."""
    print(f"[QA] Running {suite} tests...")
    return "Tests passed: 100%"

class QAAgent:
    def __init__(self):
        self.agent = Agent(
            name="qa",
            instruction="You are a QA engineer. You run automated tests.",
            tools=[run_tests]
        )
        self.server = A2AServer(self.agent, port=8002)

    def start(self):
        print("Starting QA Agent on port 8002...")
        self.server.run()

if __name__ == "__main__":
    QAAgent().start()

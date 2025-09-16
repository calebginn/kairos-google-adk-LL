"""
Demo File Agent - A minimal example for tutorial purposes.

This agent demonstrates basic file operations using the Google ADK framework.
"""
import os
import sys
from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk import Runner
from google.adk.sessions.database_session_service import DatabaseSessionService
from google.adk.memory import InMemoryMemoryService
from google.genai import types

# Import our simple file tools
from tools.file_tools import read_file, write_file, list_files

# Load environment variables
load_dotenv()

# Verify API key is available
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
if not anthropic_api_key or anthropic_api_key == "your_api_key_here":
    print("Error: ANTHROPIC_API_KEY environment variable is not set.")
    print("Please create a .env file with your API key:")
    print("ANTHROPIC_API_KEY=your_actual_api_key_here")
    sys.exit(1)

# Load agent instructions from file
def load_instructions():
    """Load instructions from the instructions.txt file."""
    instructions_path = os.path.join(os.path.dirname(__file__), "instructions.txt")
    with open(instructions_path, 'r', encoding='utf-8') as f:
        return f.read().strip()

INSTRUCTIONS = load_instructions()

# Create the agent
agent = LlmAgent(
    name="demo_file_agent",
    model=LiteLlm(
        model="anthropic/claude-3-5-sonnet-20241022",  # Using a stable model
        max_tokens=4096
    ),
    instruction=INSTRUCTIONS,
    description="A simple file management agent for demonstrations.",
    tools=[read_file, write_file, list_files]
)

# Create session and memory services
session_service = DatabaseSessionService("sqlite:///demo_sessions.db")
memory_service = InMemoryMemoryService()

# Create runner
runner = Runner(
    agent=agent,
    app_name="demo_file_agent",
    session_service=session_service,
    memory_service=memory_service
)

# Expose root_agent for ADK web server
root_agent = agent


async def run_agent(query: str, user_id: str = "demo_user", session_id: str = "demo_session"):
    """Run the agent with a query."""
    print(f"Query: {query}")
    print(f"Session ID: {session_id}")
    print("Processing...\n")

    # Create the message content
    content = types.Content(
        role='user',
        parts=[types.Part(text=query)]
    )

    # Run the agent
    events = runner.run(
        user_id=user_id,
        session_id=session_id,
        new_message=content
    )

    # Process the response
    for event in events:
        if event.is_final_response():
            response_text = event.content.parts[0].text
            print("Agent Response:")
            print(response_text)
            return response_text


if __name__ == "__main__":
    import asyncio

    # Get query from command line or use default
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = "List the files in the current directory"

    # Run the agent
    asyncio.run(run_agent(query))
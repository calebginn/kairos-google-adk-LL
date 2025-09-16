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

agent_tools = [
#    read_file, 
#    write_file, 
   list_files 
]

# Load environment variables
load_dotenv()

def get_model():
    """Get the appropriate LiteLLM model based on available API keys."""
    anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
    google_api_key = os.getenv("GOOGLE_API_KEY")
    openai_api_key = os.getenv("OPENAI_API_KEY")

    if anthropic_api_key and anthropic_api_key != "your_api_key_here":
        print("Using Anthropic Claude model")
        return LiteLlm(
            model="anthropic/claude-3-5-haiku-20241022",
            max_tokens=4096
        )
    elif google_api_key:
        print("Using Google Gemini model")
        return LiteLlm(
            model="gemini/gemini-1.5-pro",
            max_tokens=4096
        )
    elif openai_api_key:
        print("Using OpenAI GPT model")
        return LiteLlm(
            model="openai/gpt-4",
            max_tokens=4096
        )
    else:
        print("Error: No valid API key found.")
        print("Please set one of the following environment variables:")
        print("- ANTHROPIC_API_KEY=your_anthropic_api_key")
        print("- GOOGLE_API_KEY=your_google_api_key")
        print("- OPENAI_API_KEY=your_openai_api_key")
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
    model=get_model(),
    instruction=INSTRUCTIONS,
    description="A simple file management agent for demonstrations.",
    tools=agent_tools
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
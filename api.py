"""
Simple API server for the demo file agent.

This provides both HTTP API and web UI interface to the file agent.
"""
import os
import argparse
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google.adk.cli.fast_api import get_fast_api_app
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Parse command line arguments
parser = argparse.ArgumentParser(description="Start the demo file agent API server")
parser.add_argument("--disable-web-ui", action="store_true", help="Disable the ADK web UI")
parser.add_argument("--port", type=int, default=8080, help="Port to run the server on (default: 8080)")
args = parser.parse_args()

# Web UI is enabled by default, disabled only if flag is provided
enable_web_ui = not args.disable_web_ui
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
AGENT_DIR = os.path.join(BASE_DIR, "agents")  # Parent directory containing file_agent

# Create the FastAPI app using ADK's helper
app: FastAPI = get_fast_api_app(
    agents_dir=AGENT_DIR,  # Current directory contains our agent
    session_service_uri="sqlite:///demo_sessions.db",
    allow_origins=["*"],
    web=enable_web_ui  # Enable web UI by default
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "agent": "demo_file_agent"}

if __name__ == "__main__":
    print("Starting Demo File Agent API server...")
    print(f"Available at: http://localhost:{args.port}")
    print(f"Health check: http://localhost:{args.port}/health")
    print(f"Agent endpoint: http://localhost:{args.port}/run")

    if enable_web_ui:
        print(f"Web UI: http://localhost:{args.port}/")
        print("Use the web interface to chat with your file agent!")
    else:
        print("Web UI is disabled. Use API endpoints or enable with --enable-web-ui")

    print("\nPress Ctrl+C to stop the server")

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=args.port,
        reload=False
    )
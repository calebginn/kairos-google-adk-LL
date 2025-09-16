#!/usr/bin/env python3
"""
Quick start script for the demo file agent web UI.

This script checks dependencies and starts the web interface.
"""
import os
import sys
import subprocess
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed."""
    try:
        import google.adk
        import litellm
        import dotenv
        import uvicorn
        import fastapi
        return True
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("Please install dependencies with: pip install -r requirements.txt")
        return False

def check_env_file():
    """Check if .env file exists and has API key."""
    env_path = Path(".env")
    if not env_path.exists():
        print("Warning: .env file not found")
        print("Please create one with your API keys. See .env file for template.")
        return False

    # Check if API key is set
    from dotenv import load_dotenv
    load_dotenv()

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key or api_key == "your_anthropic_api_key_here":
        print("Warning: ANTHROPIC_API_KEY not set in .env file")
        print("Please add your actual API key to the .env file")
        return False

    return True

def main():
    """Main startup function."""
    print("🚀 Starting Demo File Agent Web UI...")
    print()

    # Check dependencies
    if not check_dependencies():
        sys.exit(1)

    # Check environment
    env_ok = check_env_file()
    if not env_ok:
        print("⚠️  Environment issues detected, but continuing...")
        print()

    # Start the server
    print("✅ Starting web server...")
    print("📖 Web UI will be available at: http://localhost:8080")
    print("🛑 Press Ctrl+C to stop")
    print()

    try:
        # Import and run the API
        from api import app, enable_web_ui
        import uvicorn

        if not enable_web_ui:
            print("Note: Starting with web UI enabled by default")

        uvicorn.run(
            app,
            host="0.0.0.0",
            port=8080,
            reload=False
        )
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
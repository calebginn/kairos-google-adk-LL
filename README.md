# Demo File Agent Tutorial

This is a minimal file agent implementation using the Google ADK framework. It demonstrates the basic components needed to create a file agent that can read, write, and list files.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API keys:**
   - Copy `.env` file and add your actual API keys
   - At minimum, you need an `ANTHROPIC_API_KEY`

3. **Run the agent:**

   **Option A: Command Line Interface**
   ```bash
   python agent.py "List files in the current directory"
   ```

   **Option B: Web UI Interface (Recommended for Tutorials)**
   ```bash
   # Quick start with dependency checking
   python start_web_ui.py

   # Or start directly
   python api.py
   ```
   Then open http://localhost:8080 in your browser to use the interactive web interface.

## Components

### Core Files

- **`agent.py`** - Main agent implementation with ADK setup
- **`api.py`** - HTTP API server with web UI interface
- **`start_web_ui.py`** - Quick-start script with dependency checking
- **`tools/file_tools.py`** - Basic file operation functions
- **`.env`** - Environment configuration (API keys)
- **`requirements.txt`** - Python dependencies

### Key Concepts

1. **Tools** - Python functions that the agent can call (`read_file`, `write_file`, `list_files`)
2. **Agent** - LlmAgent configured with tools and instructions
3. **Runner** - Executes the agent with session management
4. **Services** - Session and memory services for state management

## Example Usage

### Command Line Examples

```bash
# Read a file
python agent.py "Read the contents of README.md"

# Write a file
python agent.py "Write 'Hello World' to a file called hello.txt"

# List files
python agent.py "What files are in the current directory?"
```

### Web UI Examples

1. Start the server: `python api.py`
2. Open http://localhost:8080 in your browser
3. Try these prompts in the chat interface:
   - "List all files in the current directory"
   - "Create a new file called test.txt with the content 'Hello from the web UI!'"
   - "Read the contents of the file we just created"
   - "What files do we have now?"

### API Server Options

```bash
# Start with web UI (default)
python api.py

# Start without web UI (API only)
python api.py --disable-web-ui

# Use custom port
python api.py --port 9000
```

## Tutorial Notes

This demo strips away the complexity of the full repository to focus on:

- Basic ADK agent setup
- Simple tool registration
- File operations
- Session management

Perfect for learning the fundamentals before exploring more advanced features like vector stores, document processing, and streaming.
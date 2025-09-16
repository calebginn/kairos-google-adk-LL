# Demo File Agent Tutorial

This is a minimal file agent implementation using the Google ADK framework. It demonstrates the basic components needed to create a file agent that can read, write, and list files in a sandboxed workspace.

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd kairos_ll_demo
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create environment file:**
   Create a `.env` file in the root directory with one of the following API keys:
   ```bash
   # Option 1: Anthropic (Claude) - recommended
   ANTHROPIC_API_KEY=your_anthropic_api_key_here

   # Option 2: Google (Gemini)
   GOOGLE_API_KEY=your_google_api_key_here

   # Option 3: OpenAI (GPT-4)
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   The agent will automatically detect and use whichever key you provide (in that priority order).

3. **Run the agent:**

   **Option A: Command Line Interface**
   ```bash
   adk run agents/file_agent
   ```
   This starts an interactive chat session with the agent.

   **Option B: Web UI Interface (Recommended for Tutorials)**
   ```bash
   # Quick start with dependency checking
   python start_web_ui.py

   # Or start directly
   python api.py
   ```
   Then open http://localhost:8080 in your browser to use the interactive web interface.

## Components

### File Structure

```
kairos_ll_demo/
├── agents/
│   └── file_agent/
│       ├── agent.py              # Main agent implementation
│       └── instructions.txt      # Agent behavior instructions
├── tools/
│   └── file_tools.py            # File operation functions
├── agent_workspace/             # Sandboxed workspace for agent
│   └── sample.txt              # Example file
├── api.py                      # HTTP API server with web UI
├── start_web_ui.py            # Quick-start script
├── .env                       # Environment configuration (create this)
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

### Key Features

1. **Multi-Model Support** - Automatically detects and uses Anthropic Claude, Google Gemini, or OpenAI GPT-4
2. **Sandboxed Workspace** - Agent operates within `agent_workspace/` directory for safety
3. **File Operations** - Read, write, and list files with built-in tools
4. **External Instructions** - Agent behavior defined in separate `instructions.txt` file
5. **Web UI & API** - Both interactive web interface and programmatic API access

## Example Usage

### Command Line Examples

Start an interactive session with:
```bash
adk run agents/file_agent
```

Then try these prompts:
- "Read the contents of sample.txt"
- "Write 'Hello World' to a file called hello.txt"
- "What files are in the workspace?"

### Web UI Examples

1. Start the server: `python start_web_ui.py`
2. Open http://localhost:8080 in your browser
3. Try these prompts in the chat interface:
   - "List all files in the workspace"
   - "Read the sample.txt file"
   - "Create a new file called test.txt with the content 'Hello from the web UI!'"
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

## Agent Workspace

The agent operates in a sandboxed `agent_workspace/` directory containing:
- `sample.txt` - Example file for testing read operations
- Any files created by the agent will appear here
- The agent cannot access files outside this directory

## Tutorial Notes

This demo focuses on ADK fundamentals:

- Multi-model LLM integration (Claude/Gemini/GPT-4)
- Sandboxed file operations with custom tools
- External instruction configuration
- Both CLI and web interfaces
- Session and memory management

Perfect for learning core concepts before exploring advanced features like vector stores, document processing, and streaming.
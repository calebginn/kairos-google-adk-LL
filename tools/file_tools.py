"""
Basic file operation tools for the demo file agent.

This module provides simple file read and write operations.
"""
import os
from typing import Dict, Any

# Base workspace directory
WORKSPACE_DIR = "agent_workspace"


def _resolve_path(file_path: str) -> str:
    """Resolve a file path to the agent workspace directory.

    Args:
        file_path: The file path to resolve

    Returns:
        Resolved absolute path within the workspace
    """
    # Remove any leading slashes to prevent absolute path issues
    file_path = file_path.lstrip('/')

    resolved = os.path.join(WORKSPACE_DIR, file_path)

    # Ensure the base directory exists
    os.makedirs(WORKSPACE_DIR, exist_ok=True)

    return resolved


def read_file(file_path: str) -> Dict[str, Any]:
    """Read the contents of a file.

    Args:
        file_path: Path to the file to read (relative to workspace)

    Returns:
        Dictionary with either 'content' or 'error' key
    """
    try:
        resolved_path = _resolve_path(file_path)
        with open(resolved_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return {"content": content}
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except PermissionError:
        return {"error": f"Permission denied: {file_path}"}
    except Exception as e:
        return {"error": f"Error reading file: {str(e)}"}


def write_file(file_path: str, content: str) -> Dict[str, Any]:
    """Write content to a file.

    Args:
        file_path: Path to the file to write (relative to workspace)
        content: Content to write to the file

    Returns:
        Dictionary with success status or error message
    """
    try:
        resolved_path = _resolve_path(file_path)

        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(resolved_path), exist_ok=True)

        with open(resolved_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return {"success": True, "message": f"File written successfully: {file_path}"}
    except PermissionError:
        return {"error": f"Permission denied: {file_path}"}
    except Exception as e:
        return {"error": f"Error writing file: {str(e)}"}


def list_files(directory_path: str = ".") -> Dict[str, Any]:
    """List files in a directory.

    Args:
        directory_path: Path to the directory to list (relative to workspace)

    Returns:
        Dictionary with list of files or error message
    """
    try:
        resolved_path = _resolve_path(directory_path)

        if not os.path.exists(resolved_path):
            return {"error": f"Directory not found: {directory_path}"}

        if not os.path.isdir(resolved_path):
            return {"error": f"Not a directory: {directory_path}"}

        items = []
        for item in os.listdir(resolved_path):
            item_path = os.path.join(resolved_path, item)
            if os.path.isfile(item_path):
                items.append(f"📄 {item}")
            elif os.path.isdir(item_path):
                items.append(f"📁 {item}/")

        return {"items": items}
    except PermissionError:
        return {"error": f"Permission denied: {directory_path}"}
    except Exception as e:
        return {"error": f"Error listing files: {str(e)}"}
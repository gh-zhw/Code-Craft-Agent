import os
import subprocess


def create_file(file_path: str):
    """
    Create an empty file.

    Args:
        file_path (str): Path of the file to create
    """

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            pass

        return {
            "status": "success",
            "message": f"File created: {file_path}"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

def write_file(file_path: str, content: str):
    """
    Write content into a file (overwrite).

    Args:
        file_path (str): Path of the file
        content (str): Text content to write
    """

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        return {
            "status": "success",
            "message": f"Content written to {file_path}"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

def append_file(file_path: str, content: str):
    """
    Append content to a file.

    Args:
        file_path (str): Path of the file
        content (str): Text content to append
    """

    try:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(content)

        return {
            "status": "success",
            "message": f"Content appended to {file_path}"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

def read_file(file_path: str):
    """
    Read the content of a file.

    Args:
        file_path (str): Path of the file to read
    """

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        return {
            "status": "success",
            "content": content
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

def exec_shell_command(command: str, confirm: bool = True):
    """
    Execute a shell command with optional user confirmation.

    Args:
        command (str): The shell command to execute.
        confirm (bool): If True, ask the user to confirm before executing.
                        Defaults to True.

    Returns:
        dict: Contains status ("success", "error", or "cancelled") and
              command output or error message.
    """
    if confirm:
        print("\033[93m[Shell]\033[0m")
        response = input(f'Confirm to execute command `{command}` (y/n)').strip().lower()
        if response not in ('y', 'yes'):
            return {
                "status": "cancelled",
                "message": "Execution cancelled by user."
            }

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )
        return {
            "status": "success",
            "stdout": result.stdout,
            "stderr": result.stderr
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

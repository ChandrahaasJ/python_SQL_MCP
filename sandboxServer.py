from mcp.server.fastmcp import FastMCP 
from environments.loader import Auth
import sys
from pydantic import BaseModel
"""
              IMPORTANT
"""

path_to_env="REPLACE WITH ENV PATH"

mcp=FastMCP("server")

class PythonCodeInput(BaseModel):
    code: str


class PythonCodeOutput(BaseModel):
    result: str
@mcp.tool()
def query_database(query):
    """Execute a SQL query and return the results."""
    obj=Auth(path_to_env)
    cursor,conn=obj.initialize_database()
    cursor.execute(query)
    # Fetch results
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    # Clean up
    cursor.close()
    conn.close()

@mcp.tool()
def run_python_sandbox(input: PythonCodeInput) -> PythonCodeOutput:
    """Run math code in Python sandbox. Usage: run_python_sandbox|input={"code": "result = math.sqrt(49)"}"""
    import sys, io
    import math

    allowed_globals = {
        "__builtins__": __builtins__  # Allow imports like in executor.py
    }

    local_vars = {}

    # Capture print output
    stdout_backup = sys.stdout
    output_buffer = io.StringIO()
    sys.stdout = output_buffer

    try:
        exec(input.code, allowed_globals, local_vars)
        sys.stdout = stdout_backup
        result = local_vars.get("result", output_buffer.getvalue().strip() or "Executed.")
        return PythonCodeOutput(result=str(result))
    except Exception as e:
        sys.stdout = stdout_backup
        return PythonCodeOutput(result=f"ERROR: {e}")
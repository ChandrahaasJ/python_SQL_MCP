from mcp.server.fastmcp import FastMCP 
from environments.loader import Auth
import sys
path_to_env=r"C:\EAG\session8\assignment8\.env"
mcp=FastMCP("SQL_DB")


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
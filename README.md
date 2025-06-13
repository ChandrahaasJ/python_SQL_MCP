# Sandbox Environment

A secure sandbox environment for executing Python code and SQL queries through an MCP server. This environment provides a controlled space for running code with proper input validation and output capture.

## Features

1. **Python Code Execution**
   - Execute Python code in a controlled environment
   - Capture and return print statements
   - Handle both expressions and statements
   - Secure execution with controlled globals
   - Error handling and reporting

2. **SQL Query Execution**
   - Execute SQL queries against a configured database
   - Fetch and return query results
   - Proper connection management
   - Error handling for database operations

## Setup

1. **Environment Configuration**
   Create a `.env` file with the following variables:
   ```
   DBNAME=your_database_name
   DBPASS=your_database_password
   DBUSER=your_database_user
   ```

2. **Dependencies**
   ```bash
   pip install mysql-connector-python pydantic
   ```

## Usage

### Python Code Execution

```python
# Example 1: Simple expression
input = {
    "code": "result = 2 + 2"
}

# Example 2: Function definition and execution
input = {
    "code": """
def printer(ar):
    print("executed this function")

printer()
printer()
printer()
print("executed printer function thrice")
"""
}

# Example 3: Using math operations
input = {
    "code": "result = math.sqrt(49)"
}
```

### SQL Query Execution

```python
# Example: Basic SELECT query
query = "SELECT * FROM users"

# Example: INSERT operation
query = "INSERT INTO users (name, email) VALUES ('John', 'john@example.com')"
```

## Security Features

1. **Python Sandbox**
   - Controlled globals environment
   - Output capture and sanitization
   - Error handling and reporting
   - Input validation through Pydantic models

2. **SQL Execution**
   - Connection management
   - Proper resource cleanup
   - Error handling for database operations

## Project Structure

```
sandbox/
├── sandboxServer.py      # Main MCP server with execution tools
├── environments/
│   ├── loader.py        # Authentication and initialization logic
│   └── __init__.py
└── README.md
```

## Running the Server

To start the MCP server in development mode:

```bash
mcp dev sandboxServer.py
```

## Error Handling

The sandbox environment provides clear error messages for:
- Syntax errors in Python code
- Runtime errors during execution
- Database connection issues
- SQL query errors

## Contributing

Feel free to submit issues and enhancement requests!

## Security Notes

- The sandbox environment is designed for controlled execution
- All code execution is monitored and logged
- Database connections are properly managed and closed
- Input validation is performed on all operations

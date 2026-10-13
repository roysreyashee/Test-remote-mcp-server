from fastmcp import FastMCP
import random
import json


#Create fastmcp server instance 
mcp = FastMCP("Simple Calculator Server")

#Tool to add two numbers 
@mcp.tool
def add_two_numbers(a: float , b: float):
    """
    Add two numbers 

    Args: 
    a: First Number
    b: Second Number 

    Return: 
    The sum of a and b
    """

    return a + b 

#Tool to generate random numbers
@mcp.tool
def random_number(min_val: int = 1 , max_val: int = 100) -> int:
    """
    Generate a random number within a range 

    Args:
    min_val: Minimum value (default : 1)
    max_val: Maximum value (default: 100)

    Return:
    A random integer between min_val and max_val 
    """

    return random.randint(min_val, max_val)

#Resource: Server information
@mcp.resource("info://server")
def server_info() -> str :
    """Get information about this server"""
    info={
        "name": "Simple Calculator Server",
        "version": "1.1",
        "tools": ["add_two_numbers", "random_number"],
        "author": "Sreyashee"
    }

    return json.dumps(info, indent=2)

##Start the server
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000, stateless_http=True)
from fastmcp import FastMCP
import random

mcp = FastMCP("FastMCP-Server")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


@mcp.tool
def roll_dice(n_dice: int = 1) -> list[int]:
    """Roll a specified number of dice and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]


if __name__ == "__main__":
    mcp.run()
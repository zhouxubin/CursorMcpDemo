import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP('math-mcp')

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    计算两个参数的和

    Args:
        a: 第一个参数
        b: 第二个参数

    Returns:
        返回两个参数的和
    """
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """
    计算两个参数的差

    Args:
        a: 第一个参数
        b: 第二个参数

    Returns:
        返回两个参数的差
    """
    return a - b

if __name__ == "__main__":
    mcp.run()
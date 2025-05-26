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

@mcp.tool()
async def hot_news() -> str:
    """
    搜索今天的热点新闻，把所有的新闻整理输出

    Returns:
        搜索结果的总结
    """

    async with httpx.AsyncClient() as client:
        response = await client.post(
            'http://v.juhe.cn/toutiao/index',
            params={
                "type": "top",
                "key": "0f6d7a923525308e50a295401b8680b7",
                "page": 1,
                "page_size": 30
            }
        )
        
        # res_data = []
        # for data in response.json()['result']['data']:
        #     for message in choice['message']['tool_calls']:
        #         search_results = message.get('search_result')
        #         if not search_results:
        #             continue
        #         for result in search_results:
        #             res_data.append(result['content'])

        return response.text

if __name__ == "__main__":
    mcp.run()
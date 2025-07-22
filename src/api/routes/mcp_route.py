from fastmcp import FastMCP

mcp = FastMCP(name="emailmcp")

async  def start_mcp_server():
    try:
        await mcp.run_async(
            transport="streamable-http",
            host="localhost",
            port=8001
        )

    except Exception as e:
        raise
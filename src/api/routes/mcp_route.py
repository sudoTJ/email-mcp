from fastmcp import FastMCP

mcp = FastMCP(name="emailmcp")


async def start_mcp_server():
    try:
        await mcp.run_async(
            transport="streamable-http",
            host="localhost",
            port=8002
        )

    except Exception as e:
        raise


@mcp.tool(name="send_email", description="Send the email to the recipient given to you.")
async def send_email(recipient_email_address: str, subject: str, body: str) -> str:
    return f"email has been sent with subject: {subject} and body {body} to {recipient_email_address}"


@mcp.tool(name="search_email",
          description="Fetch the email on the basis of the search parameters being send.")
async def search_email(word: str) -> str:
    # sample email response
    return "searching for the email"

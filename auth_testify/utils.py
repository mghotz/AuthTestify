import aiohttp
import asyncio


class APITester:
    def __init__(self, url):
        self.url = url

    async def send_async_request(self, auth_data, payload_format="json"):
        headers = (
            {"Content-Type": "application/json"} if payload_format == "json" else {}
        )
        data = auth_data if payload_format == "json" else aiohttp.FormData(auth_data)

        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.post(self.url, data=data) as response:
                    return await self.response_parser(response)
        except aiohttp.ClientResponseError as e:
            return {"status": "error", "details": f"HTTP error: {e.status}"}
        except aiohttp.ClientConnectionError:
            return {"status": "error", "details": "Connection error"}
        except Exception as e:
            return {"status": "error", "details": f"Unexpected error: {str(e)}"}

    async def response_parser(self, response):
        status = response.status
        response_json = await response.json()
        return {"status_code": status, "content": response_json}

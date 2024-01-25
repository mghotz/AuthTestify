import aiohttp
import asyncio

async def send_async_request(url, auth_data, payload_format="form"):
    if payload_format == "json":
        data = auth_data
        headers = {'Content-Type': 'application/json'}
    else:
        data = aiohttp.FormData(auth_data)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    async with aiohttp.ClientSession(headers=headers) as session:
        try:
            async with session.post(url, data=data) as response:
                return await response_parser(response)
        except aiohttp.ClientError as e:
            return {'status': 'error', 'details': str(e)}

async def response_parser(response):
    status = response.status
    response_json = await response.json()
    return {'status_code': status, 'content': response_json}
import asyncio
from test_scenarios import basic_auth_scenarios
from utils import send_async_request

correct_credentials = {"login": "admin", "password": "admin"}

async def run_tests():
    scenarios = basic_auth_scenarios(correct_credentials)
    for scenario in scenarios:
        result = await send_async_request("http://example.com/api/auth", 
                                          {"username": scenario['login'], "password": scenario['password']})
        print("Test passed" if result == scenario['expected'] else "Test failed")

asyncio.run(run_tests())

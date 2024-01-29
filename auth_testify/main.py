import argparse
import asyncio
import logging
from test_scenarios import basic_auth_scenarios
from utils import APITester


class AuthTestify:
    def __init__(
        self,
        url,
        correct_login,
        correct_password,
        login_field,
        password_field,
        payload_format,
    ):
        self.url = url
        self.correct_login = correct_login
        self.correct_password = correct_password
        self.login_field = login_field
        self.password_field = password_field
        self.payload_format = payload_format
        self.api_tester = APITester(url)
        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
        )

    async def run_tests(self):
        logging.info("Starting authentication tests...")
        credentials = {"login": self.correct_login, "password": self.correct_password}
        fields = {"login": self.login_field, "password": self.password_field}
        scenarios = basic_auth_scenarios(credentials, fields)
        success_count = 0
        failure_count = 0

        tasks = [
            self.api_tester.send_async_request(
                {
                    self.login_field: scenario["login"],
                    self.password_field: scenario["password"],
                },
                self.payload_format,
            )
            for scenario in scenarios
        ]

        results = await asyncio.gather(*tasks, return_exceptions=True)

        for result, scenario in zip(results, scenarios):
            if isinstance(result, Exception):
                logging.error(
                    f"\033[91mError occurred: {result}\033[0m"
                )  # Red for errors
                failure_count += 1
            elif result["status_code"] == scenario["expected"]["status_code"]:
                logging.info(
                    f"\033[92mTest passed for scenario: {scenario}\033[0m"
                )  # Green for success
                success_count += 1
            else:
                logging.error(
                    f"\033[91mTest failed: Expected {scenario['expected']['status_code']}, got {result['status_code']}, payload: {scenario['login']} | {scenario['password']}\033[0m"
                )  # Red for failures
                failure_count += 1

        logging.info(
            f"All tests completed. \033[92mSuccess: {success_count}\033[0m, \033[91mFailures: {failure_count}\033[0m"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AuthTestify CLI")
    parser.add_argument(
        "--url", required=True, help="API URL for authentication testing"
    )
    parser.add_argument(
        "--login", required=True, help="Correct login credential for authentication"
    )
    parser.add_argument(
        "--password", required=True, help="Correct password for authentication"
    )
    parser.add_argument(
        "--login-field",
        default="username",
        help="Field name for login (default: username)",
    )
    parser.add_argument(
        "--password-field",
        default="password",
        help="Field name for password (default: password)",
    )
    parser.add_argument(
        "--payload-format",
        default="json",
        choices=["json", "form"],
        help="Payload format for sending credentials (default: json)",
    )

    args = parser.parse_args()

    auth_testify = AuthTestify(
        args.url,
        args.login,
        args.password,
        args.login_field,
        args.password_field,
        args.payload_format,
    )
    asyncio.run(auth_testify.run_tests())

def basic_auth_scenarios(correct_credentials):
    return [
        {
            "login": correct_credentials["login"],
            "password": correct_credentials["password"],
            "expected": {"status_code": 200},
        },
        {"login": "", "password": "", "expected": {"status_code": 400}},
        {"login": None, "password": None, "expected": {"status_code": 400}},
        {"login": 123, "password": 456, "expected": {"status_code": 401}},
        {"login": True, "password": False, "expected": {"status_code": 400}},
        {
            "login": correct_credentials["login"],
            "password": [correct_credentials["password"]],
            "expected": {"status_code": 400},
        },
    ]

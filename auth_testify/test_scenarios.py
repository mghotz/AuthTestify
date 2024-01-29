def basic_auth_scenarios(correct_credentials, fields):
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
            "login": [correct_credentials["login"]],
            "password": [correct_credentials["password"]],
            "expected": {"status_code": 200},
        },
        {
            "login": {
                fields['login']: correct_credentials["login"]
            },
            "password": {
                fields['password']: correct_credentials["password"]
            },
            "expected": {"status_code": 400},
        },
        {"login": "@dm!n", "password": "p@ssw0rd#", "expected": {"status_code": 401}},
        {
            "login": f"{correct_credentials['login']}' -- -",
            "password": "password",
            "expected": {"status_code": 401},
        },
        {
            "login": "<h1>admin</h1>",
            "password": "ololo-HTML-XSS",
            "expected": {"status_code": 400},
        },
    ]

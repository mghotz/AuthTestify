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
        {
            "login": ''.join(['\\u{:04x}'.format(ord(char)) for char in correct_credentials["login"]]),
            "password": ''.join(['\\u{:04x}'.format(ord(char)) for char in correct_credentials["password"]]),
            "expected": {"status_code": 200},
        },
        {
            "login": "ad\\nmin",
            "password": "pa\\ssword",
            "expected": {"status_code": 401},
        },
        {"login": " ", "password": " ", "expected": {"status_code": 400}},
        {"login": "a"*10000, "password": "b"*10000, "expected": {"status_code": 413}},
        {"password": correct_credentials["password"], "expected": {"status_code": 400}},
        {"login": correct_credentials["login"], "expected": {"status_code": 400}},
        {
            "login": correct_credentials["login"],
            "password": correct_credentials["password"],
            "extra": "extra",
            "expected": {"status_code": 200},
        },
        {"": "", "": "", "expected": {"status_code": 400}},
        {
            "login": correct_credentials["login"],
            "login": 'test@example.com',
            "password": correct_credentials["password"],
            "expected": {"status_code": 401},
        },
    ]

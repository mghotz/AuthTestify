
def basic_auth_scenarios(correct_credentials):
    scenarios = [
        {'login': correct_credentials['login'], 'password': correct_credentials['password'], 'expected': {'status_code': 200}},
        {'login': '', 'password': '', 'expected': {'status_code': 401}},
    ]
    return scenarios
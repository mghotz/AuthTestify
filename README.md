# AuthTestify

AuthTestify, is a sophisticated Python tool designed to streamline and enhance the testing of API authentication mechanisms. It's an essential tool for developers and testers focusing on API security, offering a robust solution for verifying the integrity and reliability of various authentication methods. AuthTestify is particularly valuable for its ability to simulate a wide range of authentication scenarios, ensuring that APIs remain secure and function correctly under diverse conditions.

This tool stands out with its versatility in handling different payload formats, such as JSON and form-data, and its capability to accommodate customized credential field names. Its CLI interface ensures ease of use and adaptability to different testing environments. AuthTestify is not just a testing tool but a comprehensive suite for API authentication assurance, making it an indispensable asset in the toolkit of modern API developers and security analysts.

The project is open for contributions, inviting collaborative development and enhancement. It's licensed under MIT, affirming its commitment to open-source community development.

## Features

- Supports JSON and form-data payloads.
- Customizable credential field names.
- Command Line Interface (CLI) for easy configuration and execution.
- Detailed logging with success and failure counts.

## Requirements

- Python 3.8+
- aiohttp

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/mghotz/AuthTestify.git
cd AuthTestify
pip install -r requirements.txt
```

## Usage

Run AuthTestify using the following command:

```bash
python auth_testify.py --url [API_URL] --login [LOGIN] --password [PASSWORD] --login-field [LOGIN_FIELD] --password-field [PASSWORD_FIELD] --payload-format [PAYLOAD_FORMAT]
```

## Future Work

- Expansion of test scenarios.
- Integration of API discovery feature.
- Continuous enhancement based on user feedback.

## Contributing

Contributions are welcome! Please refer to the issues page for feature requests and bug reports.

## License

AuthTestify is MIT licensed.

## Author

Mahammad Salimov  
Email: salimovm.7@gmail.com

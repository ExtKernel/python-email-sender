# A fork of Python Email Sender

Send emails automatically using most email service providers with this simple server in Python! 
The difference between this fork and the original repository is that we're setting up a Flask server and using environment variables here for configuration.

## Overview
The server uses the following modules:

- Flask: A lightweight WSGI web application framework used for building web applications and APIs in Python. 
- PyJWT: A Python library for working with JSON Web Tokens (JWT), which is commonly used for securely transmitting information between parties as a JSON object. 
- cryptography: A Python library that provides cryptographic recipes and primitives, often used for encrypting data, generating secure tokens, and handling key management. 
- cffi: The C Foreign Function Interface for Python, used for interfacing with C code. This module is often used indirectly through other libraries. 
- Jinja2: A templating engine for Python, used by Flask to render HTML templates. 
- Werkzeug: A comprehensive WSGI web application library used by Flask to handle the underlying HTTP protocol. 
- click: A Python package for creating command-line interfaces (CLI) with minimal code. 
- smtplib: A module for sending email using the Simple Mail Transfer Protocol (SMTP). 
- email.mime.text: A module used for creating email messages with MIME (Multipurpose Internet Mail Extensions) format, specifically for text content.

## Usage
To use this email sender, you'll need the following information:

   - The address of the SMTP server you'll be using.
   - The port number used by the SMTP server.
   - Your email account credentials.

### Make a request:
   1. Include a token in Authorization headers:
      ```json
         "Authorization": "Bearer <your-token>"
      ```
   2. Build a JSON request body. Example:
      ```json
         "subject": "subject-of-the-email",
         "message": "message-of-the-email",
         "sender_email": "sender-email",
         "sender_password": "sender-email-password",
         "recipient_email": "recipient_email"
      ```

## Install
### Bare metal
1. Clone the repository:
   ```bash
      git clone https://github.com/ExtKernel/python-email-sender
   ```
2. Navigate to the project directory:
   ```bash
      cd python-email-sender
   ```
3. Export environment variables:
   - `EXPECTED_ISSUER` - the expected issuer of the token 
   - `OAUTH2_PROVIDER_URL` - the /certs endpoint of the Oauth2 provider
   - `EXPECTED_ROLE` - the expected role that the Oauth2 user should have to access the app
   - `CLIENT_ID` - the client ID of this app from the Oauth2 provider
   - `SMPT_SERVER_ADDRESS` - SMTP server address
   - `SMTP_SERVER_PORT` - SMTP server port
4. Install requirements:
   ```bash
      pip install -r requrements.txt
   ```
5. Run the app:
   ```bash
      python app.py
   ```
   Or you can run it using:
   ```bash
      Flask run
   ```
   and specify any arguments that are applicable to the Flask command.

### Docker
1) Pull the image:
    ```bash
      docker pull exkernel/python-email-sender:<VERSION>
    ```
2) Run the container:
    ```bash
      docker run --name=win-user-sync-server -p 8000:5000 exkernel/python-email-sender:<VERSION>
    ```
   - You can map any external port you want to the internal one
   - You can give any name to the container

## Cloning / Forking

To fork my repository:
```bash
   git clone https://github.com/ExtKernel/python-email-sender
```

To fork the original repository:
```bash
   git clone https://github.com/SISSEF/python-email-sender.git 
```

This project is licensed under a [MIT](https://choosealicense.com/licenses/mit/) LICENSE.

## Feedback

If you have any feedback, you can reach out the author of the original repository at youssef@idlahsen.me

- [@SISSEF](https://github.com/SISSEF/)

Or you can reach me at dev.exkernel@gmail.com if you have a feedback about this fork specifically

- [@ExtKernel](https://github.com/ExtKernel)

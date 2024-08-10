from flask import Flask, jsonify, request
import smtplib
from email.mime.text import MIMEText

from oauth2 import token_required
from credentials import SMTP_SERVER, SMTP_SERVER_PORT

app = Flask(__name__)


def send_email(
        subject,
        message,
        sender_email,
        sender_password,
        recipient_email,
        smtp_server,
        smtp_port
):
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient_email
        server.send_message(msg)
        server.quit()
        return 'Email sent successfully!'
    except smtplib.SMTPException as e:
        raise EmailNotSent(f'Error: Email could not be sent. {e}')


@app.route('/secure/email', methods=['POST'])
@token_required
def secure_endpoint(user):
    data = request.get_json()

    if not data:
        return jsonify({'status': 'error', 'message': 'No data provided'}), 400

    required_fields = ['subject', 'message', 'sender_email', 'sender_password',
                       'recipient_email']

    for field in required_fields:
        if field not in data:
            return jsonify({'status': 'error', 'message': f'Missing required field: {field}'}), 400

    try:
        result = send_email(
            data['subject'],
            data['message'],
            data['sender_email'],
            data['sender_password'],
            data['recipient_email'],
            SMTP_SERVER,
            SMTP_SERVER_PORT
        )
        return jsonify({'status': 'success', 'message': result, 'user': user})
    except EmailNotSent as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)


class EmailNotSent(Exception):
    pass

from flask import *
import json
from random import randint
from flask_mail import Mail, Message

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    random_number = random_with_N_digits(6)
    email = str(request.args.get('email'))
    if (email != ""):
        print("start")
        send_email(email, random_number)
    data_set = {'Code': random_number, 'Email': f'{email}'}
    json_dump = json.dumps(data_set)
    return json_dump


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def send_email(email_recever, code):
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = ''
    app.config['MAIL_PASSWORD'] = ''
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail = Mail(app)
    msg = Message('Students Portal - OTP',
                  sender='emai.lrequest.api@gmail.com', recipients=[email_recever])
    msg.body = f"""

    Here is your OTP Code

    {code}
    """
    mail.send(msg)
    return


if __name__ == __name__:
    app.run(port=6766)

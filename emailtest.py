
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


if __name__ == "__main__":

    SENDGRID_API_KEY='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'
    message = Mail(
        from_email='chensiyuan0214@gmail.com',
        to_emails='chensiyuan0214@hotmail.com',
        subject='test',
        html_content='test')
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
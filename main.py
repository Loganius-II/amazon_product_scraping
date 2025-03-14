'''
Author: Logan McDermott
License: MIT

Sends you an email if a product meets certain criteria
'''

from email.message import EmailMessage
from requests_html import HTMLSession
import ssl
import smtplib
import json
from time import sleep

def send_message(subject, body, email_receiver):
    email_sender = "EMAILSENDER@gmail.com"
    email_password = 'THE EMAIL PASSWORD'
    em = EmailMessage()

    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

def load_info():
    with open("info.json", "r") as f:
        info = json.load(f)
        url = info['url']
        criteria = info['criteria']['price']
        operation = info['criteria']['operation']
        session_id = info['session-id']
        user_agent = info['user-agent']

    return url, criteria, operation, session_id, user_agent

def scrape_product():
    url, criteria, operation, session_id, user_agent = load_info()
    s = HTMLSession()
    cookies = {'session-id': session_id}
    request = s.get(url, headers={'User-Agent':user_agent,
                                  'Accept-Language': 'en-US,en;q=0.9',
                                    'Referer': 'https://www.amazon.com/'

                                  }, cookies=cookies)
    price = request.html.find('div.a-section.a-spacing-none.aok-align-center.aok-relative span.aok-offscreen', first=True).text
    price = price.replace("$", '')
    ex = eval(f"float(price) {operation} float(criteria)")
    return ex, price, criteria, operation


if __name__ == '__main__':
    email = input("Email: ")
    while True:
        ex, price, criteria, operation = scrape_product()
        if ex:
            send_message(f"Product Alert! The Current price is ${price}",f"Hello,\nThe price of the product has met the criteria!\n${price} {operation} ${criteria}", email)
            break
        else:
            sleep(30)
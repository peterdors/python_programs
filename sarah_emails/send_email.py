import smtplib
import random
import re
import sys
import time
import schedule
import urllib

from web_scraper import WebScraper
from dictionary import Dictionary
from bs4 import BeautifulSoup

def choose_random_quote(k, url):
    w = WebScraper()

    html = w.get_html(url)
    # html = urllib.urlopen(w.get_html(url)).read().decode()

    quotes = set()

    for li in html.select(k):
        for quote in li.text.split('\n'):
            # Case for handling quotes with 0 text length
            # and for handling strings of author names i.e. FirstName LastName).
            # We should never have quotes with less than two words anyway.
            if (len(quote) > 0 
            and len(quote.split()) > 3
            and quote != "Ahh!!! Still looking for more? We have something for you."):
                quotes.add(quote.strip())

    q = random.choice(list(quotes))

    return q



def prepare_email(user, pwd, recipient, subject, body):

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, TO, SUBJECT, TEXT)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pwd)
    server.sendmail(FROM, TO, message)
    server.close()

    print ('successfully sent the mail')

def send_email():
    # Declare instance of class Dictionary()
    d = Dictionary()
    # get the key
    k = d.get_key()
    # get the value
    v = d.get_website_link(k)
    # choose a random quote from the selected key and value
    quote = choose_random_quote(k, v).encode("utf8")

    print(quote)

    prepare_email(
        "senders_email_goes_here@email.com", 
        "password_goes_here",
        "receiving_email_goes_here@gmail.com", 
        "Email title/subject goes here", 
        quote)


def schedule_email_send():
    schedule.every().day.at("10:30").do(send_email)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    # if (len(sys.argv) < 3):
    #     print("Usage: python send_email.py <sender email address> <sender email password>")
    #     exit()
    schedule_email_send()

    # send_email()



    


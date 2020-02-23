import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.technopolis.bg/bg/Monitori/Monitor-SAMSUNG-LS27F354FHUXEN/p/501676'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 OPR/64.0.3417.146'
           }


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # *TODO This work as well
    #  price = soup.find(
    #     'span', {'class': 'price-value'})

    title = 'Monitor'

    price = soup.find('span', class_='price-value').get_text()
    converted_price = float(price[0:5])

    if(converted_price < 150):
        send_mail()

    print(title)
    print(converted_price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # this is the email from which the email is gonna be send
    server.login('your_mail@gmail.com', 'password!')
    subject = 'Price fell down'
    body = 'Check https://www.technopolis.bg/bg/Monitori/Monitor-SAMSUNG-LS27F354FHUXEN/p/501676 '

    msg = f"Subject: {subject} \n\n{body}"

    server.sendmail(
        'mail@gmail.com',
        'mail@gmail.com',
        msg
    )
    print('Hey, Email has been sent!')

    server.quit()


while(True):
    check_price()
    time.sleep(604800)

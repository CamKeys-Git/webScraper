import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/dp/B07S5QWM6L/ref=sr_1_1_sspa?crid=2499CKL91IZAA&keywords=macbook+pro&qid=1582839548&sprefix=Mac%2Caps%2C182&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNFlVWjVNUVlPMFlTJmVuY3J5cHRlZElkPUEwMDY3NzU3TlBIMUtXRFJMME9HJmVuY3J5cHRlZEFkSWQ9QTA0MDA5NzYyMUVDUTlGN05KSDE4JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

def find_price():
  page = requests.get(URL, headers=headers)
  soup = BeautifulSoup(page.content, 'html.parser')
  title = soup.find(id="productTitle").get_text()
  price = soup.find(id="priceblock_ourprice").get_text()
  converted_price = float(price[1:6].replace(',', '.'))

  if converted_price < 1.300:
    send_mail()
  print(converted_price)
  print(title.strip())
    

def send_mail():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('keysviolinist@gmail.com', 'christian2')

  subject = "Price reduced!"
  body = "Check this link: https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/dp/B07S5QWM6L/ref=sr_1_1_sspa?crid=2499CKL91IZAA&keywords=macbook+pro&qid=1582839548&sprefix=Mac%2Caps%2C182&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNFlVWjVNUVlPMFlTJmVuY3J5cHRlZElkPUEwMDY3NzU3TlBIMUtXRFJMME9HJmVuY3J5cHRlZEFkSWQ9QTA0MDA5NzYyMUVDUTlGN05KSDE4JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

  msg = f"Subject: {subject}\n\n {body}"
  server.sendmail('keysviolinist@gmail.com', 'camkeys@ymail.com', msg)
  print('EMAIL SENT')

  server.quit()


find_price()
# while(True):
#   find_price()
#   time.sleep(60*60)



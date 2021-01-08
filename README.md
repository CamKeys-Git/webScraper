# webScraper

## Simple web scraper using BeutifulSoup to extract prices from Amazon and email price drop updates to your gmail account.

*2021 UPDATE
Amazon has recently changed its security to block certain web scraping programs...

You will need to install requests and bs4. 

```terminal
pip install requests bs4
```

Enter a product URL here.

```python
URL = ''
```

Now paste your "user agent" to headers. You can do this by searching "my user agent" and copying it from the web.

```python
headers = {"User-Agent": '***'} # paste your user agent here
```

BeautifulSoup will parse information from from the webpage (price, title etc.). 

```python
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
```
Enter a gmail account and password here:

```python
server.login('stuff@stuff.com', 'stuff')
```

If the converted_price reaches the given threshold an email will be sent using smtplib. server.ehlo() will establish a conection between serever and email. server.sendmail will send an email from the first argument to the second argumant.

```python
def send_mail():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('stuff@stuff.com', '*****')

  subject = "Price reduced!"
  body = "Check this link: ****" #URL here

  msg = f"Subject: {subject}\n\n {body}"
  server.sendmail('stuff@stuff.com', 'stuff@stuff.com', msg)
  print('EMAIL SENT')

  server.quit()
```

Now you will need to set Google to "Allow less secure apps" in your account settings.

Choose frequency for the program to run the price check with time.sleep. (Every hour) 

```python
find_price()

while(True):
  find_price()
  time.sleep(60*60)
```

To test this out, enter a price threshold that is lower than the current price. Now run the program with:

```terminal
python webScraper.py
```

# webScraper

## Simple web scraper using BeutifulSoup to extract prices from Amazon and email automatic price updates at a given interval.

You will need to install requests and bs4. (You may also need to enable Google to "Allow less secure apps" in account settings)

Enter a product URL to parse information from (price, title etc.).

```python
URL = ''
```

If the price reaches the given threshold an email will be sent using smtplib.

```python
if converted_price < 1.300:
    send_mail()
  print(converted_price)
  print(title.strip())
```
Enter email and password here:

```python
server.login('stuff@stuff.com', '*****')
```

Choose frequency for program to run price check. 

```python
find_price()

while(True):
  find_price()
  time.sleep(60*60)
```

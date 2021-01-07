# webScraper

## Simple web scraper using BeutifulSoup to extract prices from Amazon and email automatic price updates at a given interval.

You will need to install requests and bs4

Enter a product URL to parse information from (price, title etc.).

```python
URL = ''
```

If price reaches the given threshold an email will be sent.

```
if converted_price < 1.300:
    send_mail()
  print(converted_price)
  print(title.strip())
```

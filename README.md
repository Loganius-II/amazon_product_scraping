# Product Scraper
## Overview
### A python script allows you to check if a product price on Amazon meets a certain criteria and then automatically sends you an email if it does. It uses cookies to bypass Amazons anti-scraping techniques.

### Example: Checks every 30 seconds if the $10 product has gone down in price to $9 and emails you when it goes on sale or meets that (Operation would be either == or <=)

## Setup
### Really all you need to do other than install the libraries is
- Replace line 16 of main.py with an actual email
- Replace line 17 of main.py with the code that google gives you (You need to set up SMTP on your google account)
- Replace info.json lines
  - URL with your amazon product url
  - Session-id with your browser session id cookies
  - Replace user agent with your user agent (Google "what is my user agent" then C&P)
  -  Then set an operation and price

## Conclusion
### Its a helpful automated script that helps me a lot if I am waiting for a product to go on sale or for a deal to come out and I love that I can just get emailed/notified immediately

## LET ME KNOW IF YOU HAVE ANY QUESTIONS OR COMMENTS
import smtplib
import lxml
import requests
from bs4 import BeautifulSoup

MY_EMAIL = "pypitter@gmail.com"
MY_PASS = "+28:`eEq9ML.c."

URL = "https://www.amazon.com/HUANUO-Dual-Monitor-Stand-Adjustable/dp/B07T5SY43L/ref=sr_1_5?crid=BJEBFI8UFQLY&keywords=monitor+stand&qid=1647086701&sprefix=monitor%2Caps%2C382&sr=8-5"
headers = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,ar;q=0.7,fr;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
price = float(soup.find(name="span", class_="a-offscreen").getText().split("$")[1])
print(price)

if price < 70:
    title = soup.find(name="span", id="productTitle").getText().strip()
    message = f"{title} is now at ${price}"
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=message)

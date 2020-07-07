#COVID-19 Notifier
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier

header = {"User-Agent":"Mozilla"}
req = Request("https://www.worldometers.info/coronavirus/country/india/", headers = header)
html = urlopen(req)
print(html.status)
obj = bs(html, 'lxml')

getdata = obj.findAll("div", {"class": "maincounter-number"})
cases = getdata[0].text.strip()
deaths = getdata[1].text.strip()
recovered = getdata[2].text.strip()

new_cases = obj.find("li", {"class":"news_li"}).strong.text.split()[0]
death = list(obj.find("li", {"class":"news_li"}).strong.next_siblings)[1].text.split()[0]

notifier = ToastNotifier()
# 
total =  "Cases - " + cases +"\nDeaths - " + deaths +"\nRecovered - " + recovered
message  = "New Cases - "+ new_cases+"\nNew Death - "+death

notifier.show_toast(title="COVID-19 Update\nIndia", msg=message, duration=7, icon_path=r"corona.ico")
notifier.show_toast( title="Statistics ", msg=total, duration=7, icon_path=r"corona.ico",threaded="True")



import requests
from bs4 import BeautifulSoup

hostname = "github.com"
base_url = "https://check-host.net/"
check_info_url = base_url + "ip-info"


page = requests.get(check_info_url, params={"host": hostname})
soup = BeautifulSoup(page.content, "html.parser")


csrf_token = soup.find("input", {"name": "csrf_token"})["value"]


response = requests.get(check_info_url, params={
    "host": hostname,
    "csrf_token": csrf_token
})


isp = soup.find("table" , "table-auto w-full ipinfo-table rounded").find_all("td" , "break-all","break-words")
Country = soup.find("td" , "break-words").find_all("strong")

print("IP: " + isp[0].text)
print("Hostname: " + isp[1].text)
print("ISP: " + isp[3].text)
print("Country: " + Country[0].text)



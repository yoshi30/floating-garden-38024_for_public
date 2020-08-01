import requests
from bs4 import BeautifulSoup
import re

urlName = "https://stopcovid19.metro.tokyo.lg.jp/"
infoDict = {"hospitalizedPatients" : "", "positivePatient" : ""}

def getCovidInfo():
    url = requests.get(urlName)
    soup = BeautifulSoup(url.content, "html.parser")
    infectedPerson = soup.find_all(class_ = "WhatsNew-list-item-anchor-link")
    for info in infectedPerson:
        infoText = info.text
        if "入院患者数" in infoText:
            infoDict["hospitalizedPatients"] = infoText.strip() + "だわん"
        elif "新規陽性者" in infoText:
            infoDict["positivePatient"] = infoText.strip() + "だわん"
    return infoDict


test=getCovidInfo()
print(test)
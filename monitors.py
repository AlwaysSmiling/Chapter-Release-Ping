from bs4 import BeautifulSoup, SoupStrainer
import requests
from replit import db
'''side not:
Football players are too much for one hour
Too much stamina, and too little strength control --Noel'''


class MonitorBotDS:
    def __init__(self):
        self.url = "add you webnovel's catalog url" #catalog url can be obtained by right-clicking table of content on the novel page and copying link address.
        self.strainer = SoupStrainer("a", class_="ell lst-chapter dib vam")

    def ping(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'lxml', parse_only=self.strainer)
        new_priv = soup.get_text()
        if new_priv != db["botds"]:
            db["botds"] = new_priv
            return True
        return False

class MonitorCH:
    def __init__(self):
        self.url = "add you webnovel's catalog url" #catalog url can be obtained by right-clicking table of content on the novel page and copying link address.
        self.strainer = SoupStrainer("a", class_="ell lst-chapter dib vam")

    def ping(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'lxml', parse_only=self.strainer)
        new_priv = soup.get_text()
        if new_priv != db["ch"]: 
            db["ch"] = new_priv           
            return True
        return False

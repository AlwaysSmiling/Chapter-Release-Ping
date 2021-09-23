from bs4 import BeautifulSoup, SoupStrainer
import requests
'''side not:
Football players are too much for one hour
Too much stamina, and too little strength control --Noel'''


class Monitor:
    def __init__(self, name: str, url: str):
        """Initialize the Monitor with Novel's name and url.

        Keyword arguments:
        name -- name of the novel.
        url -- url to the novel's main page.

        """
        self.name = name
        self.url = url + "/catalog"
        self.strainer = SoupStrainer("a", class_="ell lst-chapter dib vam")
        self.latestchapter = self.ini()

    def ini(self) -> str:
        """Initially called to retrieve latestchapter Chapter name at obj creation."""
        response = requests.get(self.url)
        return BeautifulSoup(response.text, 'lxml',
                             parse_only=self.strainer).get_text()

    def ping(self) -> bool:
        """Pings the Webnovel Site and return if there's a change."""
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'lxml', parse_only=self.strainer)
        chaptername = soup.get_text()
        if chaptername == "" or chaptername == self.latestchapter:
            return False
        else:
            #If new chapter is released then update self.latestchapter and return True
            self.latestchapter = chaptername
            return True
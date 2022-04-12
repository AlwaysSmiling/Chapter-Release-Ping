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
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46'}
        response = requests.get(self.url, headers=headers)
        return BeautifulSoup(response.text, 'lxml',
                             parse_only=self.strainer).get_text()

    def ping(self) -> bool:
        """Pings the Webnovel Site and return if there's a change."""
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46'}
        response = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml', parse_only=self.strainer)
        chaptername = soup.get_text()
        if chaptername == "" or chaptername == self.latestchapter:
            return False
        else:
            #If new chapter is released then update self.latestchapter and return True
            self.latestchapter = chaptername
            return True

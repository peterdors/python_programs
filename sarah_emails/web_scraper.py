import urllib
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

class WebScraper():
    
    def get_html(self, url):
        raw_html = self.get_url(url)
        # raw_html = urllib.urlopen(url).read()


        if raw_html is None:
            # Raise an exception if we failed to get any data from the url
            # raise Exception('Error retrieving contents at {}'.format(url))
            print("failed to retrieve url")
            exit()

        html = BeautifulSoup(raw_html, 'html.parser')

        return html

    def get_url(self, url):
        """
        Attempts to get the content at `url` by making an HTTP GET request.
        If the content-type of response is some kind of HTML/XML, return the
        text content, otherwise return None.
        """
        try:
            with closing(get(url, stream=True)) as resp:
            # with closing(urllib.urlopen(url)) as resp:
                if self.is_good_response(resp):
                    return resp.content
                else:
                    # print("none")
                    return None

        except RequestException as e:
            self.log_error('Error during requests to {0} : {1}'.format(url, str(e)))
            return None


    def is_good_response(self, resp):
        """
        Returns True if the response seems to be HTML, False otherwise.
        """
        content_type = resp.headers['Content-Type'].lower()
        return (resp.status_code == 200 
                and content_type is not None 
                and content_type.find('html') > -1)


    def log_error(self, e):
        """
        It is always a good idea to log errors. 
        This function just prints them, but you can
        make it do anything.
        """
        print(e)

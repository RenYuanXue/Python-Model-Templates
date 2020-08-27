# From https://www.bilibili.com/video/BV1b7411N7P2?p=32

import requests
import re

class MyCrawler():

    def __init__(self, filename):
        # File name that the crawled information will be saved as.
        self.filename = filename

    def download(self, ulr):
        r = requests.get(url)
        return r.text
    
    def extract(self, content, pattern):
        results = re.findall(pattern, content)
        return results
    
    def save(self, info):
        with open(self.filename, 'a', encoding = 'uft-8') as f:
            for item in info:
                f.write('|||'.join(item) + '\n')

    def crawl(self, url, pattern):
        content = self.download(url)
        info = self.extract(content, pattern)
        self.save(info)
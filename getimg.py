import os

from icrawler.builtin import GoogleImageCrawler

words = [
"seal","sun","soap","socks",
"turtle","tent","tiger","teacher",
"umbrella","up","umpire","uncle",
"violin","vet","vest","van",
]

for word in words:
    os.makedirs('img/'+word, exist_ok=True)
    google_crawler = GoogleImageCrawler(storage={'root_dir': 'img/'+word})
    google_crawler.crawl(keyword=word, max_num=3)

import os

from icrawler.builtin import GoogleImageCrawler

words = [
    "wolf","web","water","watch",
    "fox","box","six","wax",
    "yoyo", "yak", "yogurt", "yacht",
    "zipper", "zero", "zoo", "zebra"
]

for word in words:
    os.makedirs('img/'+word, exist_ok=True)
    google_crawler = GoogleImageCrawler(storage={'root_dir': 'img/'+word})
    google_crawler.crawl(keyword=word, max_num=2)

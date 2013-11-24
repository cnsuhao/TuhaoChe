import os
import requests
import json

def getTimeline():
    url="https://api.weibo.com/2/statuses/home_timeline.json?count=100&access_token=2.00tzWGVD_MPhfC7a56234d8dBWk2SC"
    text_data = requests.get(url)
    data = json.loads(text_data.text)
    print len(data["statuses"])


def main():
    getTimeline()

if __name__=="__main__":
    main()

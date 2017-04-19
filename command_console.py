"""    A simple news_api application that uses aljazera api to pick the latest news from google 
        
"""
import json
import sys, os
import http.client


def call_news_api():
    conn = http.client.HTTPSConnection("newsapi.org")
    conn.request("GET", "/v1/articles?source=al-jazeera-english&sortBy=top&apiKey=67e1e2377a864dfeb26d89d3847b02e8")

    response = json.loads(conn.getresponse().read().decode())
    os.system('clear')
    print("Latest News and Updates on aljazera ")
    print("....................................")

    for news in response['articles']:
        print(Colors.OKGREEN + news['title'] + Colors.ENDC + "\n", news['description'] + "\n", news['publishedAt'])


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


call_news_api()
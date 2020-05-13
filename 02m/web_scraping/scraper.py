import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/news')
soup_obj = BeautifulSoup(response.text, 'html.parser')
links = soup_obj.select('.storylink')
subtext = soup_obj.select('.subtext')


def sort_stories(news_list):
    return sorted(news_list, key=lambda k: k['Votes'], reverse=True)


def create_custom_news(links, votes):
    news_list = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                news_list.append(
                    {'Title': title, 'Link': href, 'Votes': points})

    return sort_stories(news_list)


pprint.pprint(create_custom_news(links, subtext))

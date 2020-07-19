import requests
from bs4 import BeautifulSoup
import pprint
from time import sleep


def loop_pages():
    total_list = []
    pages = int(input('Tell me how many pages do you wanna I check: '))
    for page in range(1, pages+1):
        res = requests.get(f'https://news.ycombinator.com/news?p={page}')
        soup = BeautifulSoup(res.text, 'html.parser')
        links = (soup.select('.storylink'))
        subtext = soup.select('.subtext')
        actual_list = (create_custom_hn(links, subtext))
        total_list.extend(actual_list)
        sleep(30)
    total_list = sort_stories_by_votes(total_list)
    pprint.pprint(total_list)


def sort_stories_by_votes(hn_list):
    return sorted(hn_list, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


loop_pages()

#!/Users/jamesonwelch/env/bin/Python3

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import ssl
import argparse

# Command Line Interface Configuration
parser = argparse.ArgumentParser(description='Top 2 headlines from the Wall Street Journal')
#parser.add_argument('Main headline', type=int, help='Show main headline only')
#args = parser.arse_args()
group = parser.add_mutually_exclusive_group()
group.add_argument('-m', '--main', action='store_true', help='Print main headline only')
group.add_argument('-s', '--summary', action='store_true', help='Print main headline with summary')
group.add_argument('-a', '--all', action='store_true',help='Print all content')

args = parser.parse_args()

wsj_url = 'https://www.wsj.com/'
context = ssl._create_unverified_context()
# Open connection, grab page
uClientWsj = uReq(wsj_url, context=context)
wsj_html = uClientWsj.read()
uClientWsj.close()

# Parse HTML
page_soup = soup(wsj_html, 'html.parser')
containers = page_soup.findAll('div', {'class':'LS-LEAD-NO-IMAGE'})
containers_sec = page_soup.findAll('div', {'class':'LS-SECONDARY-BIG-IMAGE'})

for container in containers:
    headline_title = container.h3.a.text
    summary_text = container.div.span.text

    # print (headline_title)
    # print (summary_text)

for container in containers_sec:
    headline_title_sec = container.h3.a.text


if __name__ == '__main__':
    if args.main:
        print(headline_title)
    elif args.summary:
        print(headline_title, '\n', summary_text)
    elif args.all:
        print(headline_title, '\n', summary_text, '\n', headline_title_sec)
    else:
        print(headline_title, '\n', summary_text, '\n', headline_title_sec)

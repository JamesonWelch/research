from flask import Flask, render_template
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

app = Flask(__name__)

wsj_url = 'https://www.wsj.com/'

# Open connection, grab page
uClientWsj = uReq(wsj_url)
wsj_html = uClientWsj.read()
uClientWsj.close()

# Parse HTML
page_soup = soup(wsj_html, 'html.parser')
containers = page_soup.findAll('div', {'class':'LS-LEAD-NO-IMAGE'})

# Need to grab 'wsj-headline-link' text
# Need to grab 'wsj-card-body' text

for container in containers:
    headline_title = container.h3.a.text
    summary_text = container.div.span.text

    print (headline_title)
    print (summary_text)

@app.route('/news.html')
def news_page():
    render_template('news.html', the_title='Current Top Headlines')

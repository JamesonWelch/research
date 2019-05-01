from flask import Flask, render_template
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import ssl

app = Flask(__name__)

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

# Need to grab 'wsj-headline-link' text
# Need to grab 'wsj-card-body' text

for container in containers:
    headline_title = container.h3.a.text
    summary_text = container.div.span.text

    # print (headline_title)
    # print (summary_text)

for container in containers_sec:
    headline_title_sec = container.h3.a.text

@app.route('/news.html')
def news_page():
    return render_template('news.html',
                            titles = 'The Wall Street Journal',
                            the_title ='Current Top Headlines',
                            headline_title = headline_title,
                            summary_text = summary_text,
                            headline_title_sec = headline_title_sec,)


if __name__ == '__main__':
    app.run(debug=True)

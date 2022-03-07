from flask import Flask
import feedparser

app = Flask(__name__)
RSS_FEEDS = dict(bbc='http://feeds.bbci.co.uk/news/rss.xml',
                 cnn='http://rss.cnn.com/rss/edition.rss',
                 fox='http://feeds.foxnews.com/foxnews/latest',
                 iol='http://www.iol.co.za/cmlink/1.640')
# BBC_FEED = 'https://feeds.bbci.co.uk/news/rss.xml'

@app.route('/')
@app.route('/<source>')
# def bbc():
#     return get_news('bbc')
#
# @app.route('/cnn')
# def cnn():
#     return get_news('cnn')
#
# @app.route('/fox')
# def fox():
#     return get_news('fox')
#
# @app.route('/iol')
# def iol():
#     return get_news('iol')

def get_news(source='bbc'):
    feed = feedparser.parse(RSS_FEEDS[source])
    first_article = feed['entries'][0]
    return """<html>
      <body>
        <h1>  Headlines </h1>
        <b> {0} </b> <br/>
        <i> {1} </i> <br/>
        <p> {2} </p> <br/>
      </body>
    </html>
    """.format(first_article.get('title'),first_article.get('published'), first_article.get('summary'))



if __name__ == '__main__':
    app.run(port=5000,debug=True)
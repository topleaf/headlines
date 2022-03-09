from flask import Flask, render_template, request
import feedparser

app = Flask(__name__)
# https://rss.com/blog/popular-rss-feeds/

RSS_FEEDS = dict(bbc='http://feeds.bbci.co.uk/news/rss.xml',
                 bbcasia='http://feeds.bbci.co.uk/news/world/asia/rss.xml',
                 nytimes='https://rss.nytimes.com/services/xml/rss/nyt/AsiaPacific.xml',
                 cnn='http://rss.cnn.com/rss/edition.rss',
                 fox='http://feeds.foxnews.com/foxnews/latest',
                 latimesworld='https://www.latimes.com/world/rss2.0.xml',
                 iol='http://www.iol.co.za/cmlink/1.640',
                 dwworld='http://rss.dw.com/rdf/rss-en-world',
                 dwasia='http://rss.dw.com/rdf/rss-en-asia',
                 dwscience='http://rss.dw.com/xml/rss_en_science',
                 dwculture='http://rss.dw.com/rdf/rss-en-cul')
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

    query = request.args.get('source')

    if not query or query.lower() not in RSS_FEEDS:
        source = 'bbcasia'
    else:
        source = query.lower()

    feed = feedparser.parse(RSS_FEEDS[source])
    articles = feed['entries']

    return render_template('home.html', source=source, articles=articles)
    # dynamic
    # first_article = feed['entries'][0]
    # return render_template('home.html', source=source, title=first_article.get('title'),
    #                        published=first_article.get('published'),
    #                        summary=first_article.get('summary'))

    # static
    # return """<html>
    #   <body>
    #     <h1>  Headlines </h1>
    #     <b> {0} </b> <br/>
    #     <i> {1} </i> <br/>
    #     <p> {2} </p> <br/>
    #   </body>
    # </html>
    # """.format(first_article.get('title'),first_article.get('published'), first_article.get('summary'))



if __name__ == '__main__':
    app.run(port=5000,debug=True)
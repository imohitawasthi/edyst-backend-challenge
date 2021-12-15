from flask import render_template, request, redirect

from src import app, db, redis_queue
from src.models.CrawledPage import CrawledPage
from src.utils.utils import count_words_at_url


@app.route('/')
def index_crawled_page():
    crawled_pages = CrawledPage.query.order_by(CrawledPage.created_at.desc()).all()
    return render_template('index.html', crawled_pages=crawled_pages)


@app.route('/crawled-pages', methods=['POST'])
def create_crawled_page():
    page_name = request.form['page_name']
    page_url = request.form['page_url']

    # Call to the redis queue
    job = redis_queue.enqueue_call(
        count_and_save_words, args=[page_name, page_url], result_ttl=5000
    )

    return redirect('/')


def count_and_save_words(name, url):
    word_count = count_words_at_url(url)

    new_crawled_page = CrawledPage(name=name, url=url, word_count=word_count)
    try:
        db.session.add(new_crawled_page)
        db.session.commit()
    except:
        print("Something went wrong")

    return new_crawled_page.id

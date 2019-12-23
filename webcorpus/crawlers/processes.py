
import os
import shutil
import logging
import threading

from scrapy import signals
from scrapy.crawler import CrawlerProcess
from .w3newspaper import W3NewsPaperSpider
from .news import makecrawler
from ..sources import Sources
from ..language import name2code
from ..utils import extract_domain
from urllib.parse import urljoin
from datetime import datetime


logging.getLogger('scrapy').propagate = False
logging.getLogger('urllib3').propagate = False


def get_sources(srcdir, languages):
    process = CrawlerProcess()
    process.crawl(W3NewsPaperSpider, languages=languages)
    crawler = list(process.crawlers)[0]
    callback = lambda spider: write_sources(srcdir, spider.sources)
    crawler.signals.connect(callback, signals.spider_closed)
    process.start()


def write_sources(srcdir, urls):
    for lang in urls:
        code = name2code(lang)
        sources = Sources(srcdir, code)
        for url in urls[lang]:
            source = {
                'name': extract_domain(url),
                'home_url': url,
                'sitemap_url': urljoin(url, 'sitemap.xml')
            }
            sources.add(**source)


def fetch_corpus(lang, output_path, srcdir, jobdir_root, **crawler_settings):

    sources = Sources(srcdir, lang).all()

    print("Crawling sources: ", ', '.join(sources.keys()))

    # create job directories
    jobdirs = {}
    lang_root = os.path.join(jobdir_root, 'current', lang)
    for name in sources:
        jobdir = os.path.join(lang_root, name)
        jobdirs[name] = jobdir
        os.makedirs(jobdir, exist_ok=True)

    while True:
        process = CrawlerProcess(settings=crawler_settings)
        for source in sources.values():
            crawler = makecrawler(source, srcdir, JOBDIR=jobdirs[name])
            if crawler:
                process.crawl(crawler, source=source, corpus_path=output_path)
        stats = ScrapingStats(process.crawlers)
        stats.print_stats()
        process.start()  # block until all crawling jobs are finished
        print('Creating Checkpoint...')
        chkpt_id = datetime.now().strftime('%H%M_%d%m')
        path = os.path.join(jobdir_root, 'ckp_{}_{}'.format(lang, chkpt_id))
        shutil.copytree(lang_root, path)


class ScrapingStats:
    """
    Display scraping stats
    """

    def __init__(self, crawlers):
        self.crawlers = crawlers

    def print_stats(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Stats: ')
        for crawler in self.crawlers:
            spider = crawler.spider
            if hasattr(spider, 'name') and hasattr(spider, 'arts_collected'):
                print('{}: {} articles'.format(spider.name,
                                               spider.arts_collected))
        threading.Timer(15.0, self.print_stats).start()
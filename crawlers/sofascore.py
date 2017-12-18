# -*- coding: utf-8 -*-

import crawlers
from datetime import date


class SofaScoreCrawler(crawlers.Crawler):

    def get_current_games(self):
        json = self.get_json(url='football//' + date.isoformat(date.today()) + '/json')
        pass


# debug
if __name__ == '__main__':
    crawler = SofaScoreCrawler(base_url='https://www.sofascore.com/')
    crawler.get_current_games()
# -*- coding: utf-8 -*-

import crawlers
from datetime import date


class SofaScoreCrawler(crawlers.Crawler):

    def get_tournaments(self):
        json = self.get_json(url='football//' + date.isoformat(date.today()) + '/json')
        tournaments = []
        for tournament in json['sportItem']['tournaments']:
            tournaments.append(tournament['tournament']['name'])
        return tournaments


# debug
if __name__ == '__main__':
    crawler = SofaScoreCrawler(base_url='https://www.sofascore.com/')
    crawler.get_tournaments()
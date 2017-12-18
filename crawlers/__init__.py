# -*- coding: utf-8 -*-

import config
import random
import requests
from lxml import html


class Crawler:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_tournaments(self):
        raise NotImplementedError('Method get_current_games is not implemented')

    def get(self, url):
        headers = {
            'User-agent': random.choice(config.user_agents)
        }
        return requests.get(self.base_url + url, proxies=config.proxies, headers=headers)

    def get_html(self, url):
        response = self.get(url=url)
        return html.fromstring(response.content) if response.status_code == 200 else False

    def get_json(self, url):
        response = self.get(url=url)
        return response.json() if response.status_code == 200 else False
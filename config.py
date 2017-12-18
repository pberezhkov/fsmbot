# -*- coding: utf-8 -*-

token = ''
try:
    f = open('.token', 'r')
    token = f.read()
    f.close()
except FileNotFoundError:
    print('Token file not found')

proxies = {
    'http': 'socks4://127.0.0.1:9050',
    'https': 'socks4://127.0.0.1:9050'
}

user_agents = (
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
)

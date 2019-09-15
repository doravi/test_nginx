from test import *

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1'
]

url = "nginx"
port = "80"


class Run:
    def __init__(self, url, port, user_agents):
        self.url = url
        self.port = port
        self.user_agents = user_agents

    def main(self):
        for userAgent in user_agents:
            test_http_v11_get(self.url, self.port, userAgent)
            test_http_v11_post(self.url, self.port, userAgent)
            test_http_v10_get(self.url, self.port, userAgent)
            test_http_v10_post(self.url, self.port, userAgent)


if __name__ == '__main__':
    Run(url, port, user_agents).main()

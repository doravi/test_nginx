import httplib
import urllib
import requests


def test_http_v11_get(url, port, userAgent):
    print("testing GET ngnix with HTTP/1.1 with userAgent: " + userAgent)
    response = requests.get("http://" + url + ":" + port,
                            headers={"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain",
                                     'User-Agent': userAgent})
    if response.status_code is 200:
        print response.status_code, response.reason
    else:
        print response.status_code, response.reason


def test_http_v11_post(url, port, userAgent):
    print("testing POST ngnix with HTTP/1.1 with userAgent: " + userAgent)
    response = requests.post("http://" + url + ":" + port, data={"test": "test"},
                             headers={"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain",
                                      'User-Agent': userAgent})
    if response.status_code is 200:
        print response.status_code, response.reason
    else:
        print response.status_code, response.reason


def test_http_v10_get(url, port, userAgent):
    print("testing GET ngnix with HTTP/1.0 with userAgent: " + userAgent)
    httplib.HTTPConnection._http_vsn = 10
    httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'

    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", 'User-Agent': userAgent}
    conn = httplib.HTTPConnection(url, port, headers)
    conn.request("GET", "/")
    r1 = conn.getresponse()
    print r1.status, r1.reason
    conn.close()


def test_http_v10_post(url, port, userAgent):
    print("testing POST ngnix with HTTP/1.0 with userAgent: " + userAgent)
    httplib.HTTPConnection._http_vsn = 10
    httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'

    params = urllib.urlencode({'test': 'test'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", 'User-Agent': userAgent}
    conn = httplib.HTTPConnection(url, port)
    conn.request("POST", "/", params, headers)
    response = conn.getresponse()
    print response.status, response.reason

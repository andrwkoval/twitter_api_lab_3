import urllib.request
import urllib.parse
import urllib.error
import twurl
import json
import ssl


def get_js_data(username, users):

    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = twurl.augment(TWITTER_URL,
                        {'screen_name': username, 'count': '{}'.format(users)})

    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    js = json.loads(data, encoding="utf-8")

    return js

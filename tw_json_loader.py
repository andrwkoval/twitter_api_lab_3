import urllib.request
import urllib.parse
import urllib.error
import twurl
import json
import ssl


def get_js_data(username, users):
    """
    (str, int) -> json(dict)
    This function gets twitter username and amount of friends to
    display and creates json file with information about user friends.
    username: twitter username
    users: amount of users to be displayed
    returns: json data with information about user friends
    """

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

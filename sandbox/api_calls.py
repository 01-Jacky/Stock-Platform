import urllib.request
import json


def get_json(url_endpoint):
    """
    Returns the html of url or None if status code is not 200
    """
    req = urllib.request.Request(
        url_endpoint,
        headers={
            'User-Agent': 'Python Learning Program',
            'From': 'hklee310@gmail.com'
        }
    )
    resp = urllib.request.urlopen(req)

    if resp.code == 200:
        json_content = resp.read()
        return json.loads(json_content)
    else:
        raise ConnectionError('API endpoint did not return a 200')

if __name__ == "__main__":
    endpoint = 'https://api.iextrading.com/1.0/stock/aapl/chart/1y'
    json = get_json(endpoint)

    print(len(json))
    # x = json[0]
    print(json[30]['close'])


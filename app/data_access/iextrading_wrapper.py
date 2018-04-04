"""
source: https://iextrading.com/developer/docs/#chart
e.g.
/stock/aapl/chart
/stock/aapl/chart/5y
/stock/aapl/chart/2y
/stock/aapl/chart/1y
/stock/aapl/chart/ytd
/stock/aapl/chart/6m
/stock/aapl/chart/3m
/stock/aapl/chart/1m
/stock/aapl/chart/1d
/stock/aapl/chart/date/20170919 ***
/stock/aapl/chart/dynamic

*** date endpoint is broken. Need to determine the smallest endpoint we can call on to get the data.
e.g. if closing is 25 days out, call on the 1 month endpoint
"""

import urllib.request
import json
from datetime import datetime
import logging
import time

logging.basicConfig(level=logging.INFO,
                    # format='%(asctime)s %(levelname)s %(message)s',
                    format='%(levelname)s %(message)s',
                    # filename='/tmp/myapp.log',
                    filemode='w')

CHARTS_URL = 'https://api.iextrading.com/1.0/stock/{ticker}/chart/{date_interval}'

def _iex_chart_endpoint(ticker, date_interval):
    """
    Returns the json of the charts endpoint
    """
    start = time.time()

    url_endpoint = CHARTS_URL.format(ticker=ticker, date_interval=date_interval)
    req = urllib.request.Request(
        url_endpoint,
        headers={
            'User-Agent': 'Python Learning Program',
            # 'From': 'suchandsuch@email.com'
        }
    )
    resp = urllib.request.urlopen(req)


    logging.debug('Attempting Request URL: ' + url_endpoint)
    if resp.code == 200:
        stop = time.time()
        # print(stop - start)

        json_content = resp.read()
        logging.debug('Received 200')
        return json.loads(json_content)
    else:
        logging.debug('Did not get 200')
        raise ConnectionError('Source: iextrading_wrapper. API endpoint did not return a 200')


def close_price(ticker, datetime_obj):
    """
    get close price on specific date
    To-Do: Pick the shortest date range option
    """
    start = time.time()

    # Fast enough to just pull 5 years and iterate through to find the date we want.
    # If price for date falls on non-market day, use the next one
    json = _iex_chart_endpoint(ticker, '5y')
    date_data = None

    search_count = 0
    for i in range(len(json)):
        el_date = json[i]['date']
        el_date = datetime.strptime(el_date, "%Y-%m-%d")

        days_delta = (datetime_obj - el_date).days

        if days_delta == 0:
            logging.debug('Found date {}'.format(json[i]['date']))
            date_data = json[i]
            break
        elif days_delta < 0:
            if i+1 < len(json):
                logging.debug('Missing date, skip forward to {}'.format(json[i]['date']))
                date_data = json[i+1]
                break
        search_count += 1

    if date_data is None:
        logging.debug('Missing date, no next date')
        raise ValueError('Error: can not find data for {} from iextrading chart'.format(
            datetime_obj.date()))


    stop = time.time()
    # print(stop - start)

    logging.debug('Itreated through {} items'.format(search_count))
    return date_data['close']



if __name__ == '__main__':
    # Test out getting price for a date
    # date_string = '2017-10-31'
    # date = datetime.strptime(date_string, "%Y-%m-%d")
    # close_price = close_price('amzn', date)
    # print('Price = {}'.format(close_price))

    # Test out getting a return
    start = time.time()

    ticker = 'fb'
    buy_date = '2018-03-22'
    sell_date = '2018-03-29'

    buy_date_price = close_price(ticker, datetime.strptime(buy_date, "%Y-%m-%d"))
    today_price = close_price(ticker, datetime.strptime(sell_date, "%Y-%m-%d"))

    percent_gain = ((today_price/buy_date_price) - 1) * 100

    print('Purchase: {} | Sold {}:'.format(buy_date_price,today_price))
    print('Precent gain = {}'.format(percent_gain))

    stop = time.time()
    print(stop-start)
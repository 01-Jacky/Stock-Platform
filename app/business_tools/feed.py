import sys
sys.path.append('..')   # Add parent folder path to sys.path

import datetime

from data_access import data_accessor
from data_access import constants


def close_price(ticker, date, datasource=constants.IEXTRADING):
    close = data_accessor.get_close(ticker, date, datasource)
    return close


if __name__ == '__main__':
    date_string = '2018-01-12'
    date1 = datetime.datetime.strptime(date_string, "%Y-%m-%d").strftime("%d-%m-%Y")
    print(date1)
    # close_price = close_price('aapl', 'need date here')
    # print(close_price)
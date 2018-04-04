import datetime

import iextrading_wrapper
import constants

def get_close(ticker, date, datasource=constants.IEXTRADING):
    if datasource == constants.IEXTRADING:
        close_price = iextrading_wrapper.close_price(ticker, date)
        return close_price
    else:
        raise ValueError('Error at data acessor: Datasource not recognized')


if __name__ == '__main__':
    close_price = get_close('aapl', 'need date here')
    print(close_price)
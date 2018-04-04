import datetime
import sys
sys.path.append('..')   # Add parent folder path to sys.path

from business_tools import feed



def close_price_change(ticker, start_date, end_date):
    start_price = feed.close_price(ticker, start_date)
    end_price = feed.close_price(ticker, end_date)

    return start_price - end_price


def closing_time_series(ticker, start_date, end_date):
    pass


def main():
    # Test price_change date range
    ticker = 'aapl'
    date_string = '2018-01-12'
    start_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")    # Last part strips the hh:mm:ss
    days_gap = 7
    end_date = start_date + datetime.timedelta(days=days_gap)



    # close_price = close_price_change(ticker, start_date, end_date)
    # print(close_price)


if __name__ == "__main__":
    try:
        main()
    except ConnectionError as e:
        print('Error: {}'.format(e))
    except ValueError as e:
        print('Error: {}'.format(e))


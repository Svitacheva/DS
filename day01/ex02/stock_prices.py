import sys


def get_stock_price():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    if len(sys.argv) != 2:
        sys.exit(1)

    company = sys.argv[1].capitalize()
    ticker = COMPANIES.get(company)

    if ticker:
        print(STOCKS[ticker])
    else:
        print(f"Unknown company")


if __name__ == '__main__':
    get_stock_price()

import pandas as pd
import requests

class Data:

    def __init__(self, date_start, date_end):

        self.date_start_int = date_start
        self.date_end_int = date_end

    def master_df(self):

        avail_pairs = Data.get_avail_universe_pairs()

        master_data = pd.DataFrame()

        for i in avail_pairs:

            data = pd.DataFrame(requests.get(
                    "https://poloniex.com/public?command=returnChartData&currencyPair={}&start={}&end={}&period=300".format(
                        i, self.date_start_int, self.date_end_int)).json())
            data['Pair'] = i

            master_data = master_data.append(data)

        return master_data


    @staticmethod
    def get_avail_universe_pairs():

        tickers = pd.DataFrame(requests.get("https://poloniex.com/public?command=returnTicker").json())

        avail_pairs = []
        avail_pairs.append('USDT_BTC')
        for i in tickers.columns:
            if i[0:4] == 'BTC_':
                avail_pairs.append(i)

        return avail_pairs


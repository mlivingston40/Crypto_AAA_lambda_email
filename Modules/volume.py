import pandas as pd


def relevant_universe_list(coin_filter, df, start_date, end_date):
    # This will turn the relevant universe for each iteration through the trade_days dataframe #
    # Which will then be used to feed the analytics in the trades.py module #

    print(len(df))

    # This will already be in memory - the master dataframe from class Data #
    df_vol = df[(df.date >= start_date) & (df.date <= end_date)]

    pairs = df_vol.groupby('Pair').agg({'volume': 'count'})
    # Probably want to bake in a filter for pairs that aren't there for the whole past volume_window_days_ #

    coin_volume = []
    for i in pairs.index:
        data = df_vol[df_vol['Pair'] == i]
        avg = data.volume.sum() / len(data)
        coin_volume.append({'coin': i, 'avg_vol': avg})
    coin_volume = pd.DataFrame(coin_volume)

    # sort for top based upon 'universe_amt' parameter and return the list #

    return coin_volume.sort_values(by=['avg_vol'], ascending=False).head(coin_filter)

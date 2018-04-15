import pandas as pd


def top_momentum_df(rel_universe, num_coins_allocate, df, start_date, end_date):

    # This will already be in memory - the master dataframe from class Data #
    df_mom = df[(df.date >= start_date) & (df.date <= end_date)]


    returns = []
    for i in rel_universe.coin:

        mom = (df_mom[df_mom.Pair == i].weightedAverage.tail(1).values - df_mom[
            df_mom.Pair == i].weightedAverage.head(1).values) / df_mom[df_mom.Pair == i].weightedAverage.head(
            1).values

        returns.append({'Pair': i, 'Momentum': mom[0]})

    returns = pd.DataFrame(returns)

    top_returns = returns.sort_values(by=['Momentum'], ascending = False).head(num_coins_allocate)

    # account for only positive momentum #

    return top_returns[top_returns.Momentum > 0]

from Modules.momentum import *
from Modules.poloniex import *
from Modules.volume import *
from Modules.email import *

import datetime
from datetime import timedelta


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def lambda_handler(event, context):

    now_ts = datetime.datetime.now()
    now_ts_int = int(now_ts.strftime("%s"))

    #-70
    vol_lb_ts = now_ts + timedelta(days=-4)
    vol_lb_ts_int = int(vol_lb_ts.strftime("%s"))

    #21
    mom_lb_ts = now_ts + timedelta(days=-2)
    mom_lb_ts_int = int(mom_lb_ts.strftime("%s"))

    master_data = Data(vol_lb_ts_int, now_ts_int).master_df()

    rel_universe = relevant_universe_list(20, master_data, vol_lb_ts_int, now_ts_int)

    top_mom_coins = top_momentum_df(rel_universe, 10, master_data, mom_lb_ts_int, now_ts_int)

    if len(top_mom_coins) == 0:

        top_mom_coins = top_mom_coins.append({'Pair': 'USDT_BTC',
                                              'Momentum': "No coins with momentum"}, ignore_index=True)

    else:
        pass

    send_email('email', 'pw',
               "recipients",
               "Crypto AAA Automated Daily Email", top_mom_coins)

    print(top_mom_coins)
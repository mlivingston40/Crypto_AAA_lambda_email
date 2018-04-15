from Modules.momentum import *
from Modules.poloniex import *
from Modules.volume import *

import datetime
from datetime import timedelta

def lambda_handler():

    now_ts = datetime.datetime.now()
    now_ts_int = int(now_ts.strftime("%s"))

    vol_lb_ts = now_ts + timedelta(days=-70)
    vol_lb_ts_int = int(vol_lb_ts.strftime("%s"))

    #21
    mom_lb_ts = now_ts + timedelta(days=-10)
    mom_lb_ts_int = int(mom_lb_ts.strftime("%s"))

    master_data = Data(vol_lb_ts_int, now_ts_int).master_df()

    rel_universe = relevant_universe_list(20, master_data, vol_lb_ts_int, now_ts_int)

    print(top_momentum_df(rel_universe, 12, master_data, mom_lb_ts_int, now_ts_int))
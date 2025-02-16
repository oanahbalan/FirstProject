import os
import sys

sys.path.append((os.path.dirname(os.getcwd())))  # Append path to dock_daily_profit

import dock_weekly_profit_utils as utils

if __name__ == "__main__":
    utils.dock_management()

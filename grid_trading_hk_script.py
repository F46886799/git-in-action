from utils import *
import time

if __name__ == "__main__":
    # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNDY4ODY3OTlAMTYzLmNvbSIsImV4cGlyZXMiOjE3Nzk4Nzc5NjkuNDU3MTM2Mn0.NF1ynVWX_OhXo_UOP-DAc8lyNUDT29_2BCfbQIn8uRc
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNDY4ODY3OTlAMTYzLmNvbSIsImV4cGlyZXMiOjE3Nzk4Nzc5NjkuNDU3MTM2Mn0.NF1ynVWX_OhXo_UOP-DAc8lyNUDT29_2BCfbQIn8uRc',
        'Content-Type': 'application/json',
    }
    logger.info("***Step1:Hello World,{}".format(get_current_time()))
    requests_get('http://dreamtown.synology.me:5184', headers)
    logger.info("\n")

    time.sleep(1)

    logger.info("***Step2:Download Data,{}".format(get_current_time()))
    download_data = {
        "start_date": "2023-08-21",
        "end_date": "2030-12-31",
        "source": "akshare_stock",
        "freq": "1d"
    }
    requests_post('http://dreamtown.synology.me:5184/grid/data', headers, download_data)
    logger.info("\n")

    time.sleep(1)

    logger.info("***Step3:Generate Signals：腾讯控股,{}".format(get_current_time()))
    signal_data = {
          "start_date": "2023-08-21",
          "end_date": "2030-12-31",
          "backtest_config": "grid_tencent_1d",
          "stock_abbr": "tencent",
          "strategy_name": "trend_following",
          "grid_low": 6.25,
          "grid_high": 10.35,
          "grid_num": 6
    }
    requests_post('http://dreamtown.synology.me:5184/grid/signals', headers, signal_data)
    logger.info("\n")

    logger.info("***Step3:Generate Signals：小米集团,{}".format(get_current_time()))
    signal_data = {
          "start_date": "2023-08-21",
          "end_date": "2030-12-31",
          "backtest_config": "grid_xiaomi_1d",
          "stock_abbr": "xiaomi",
          "strategy_name": "trend_following",
          "grid_low": 6.25,
          "grid_high": 10.35,
          "grid_num": 6
    }
    requests_post('http://dreamtown.synology.me:5184/grid/signals', headers, signal_data)
    logger.info("\n")
    
    logger.info("***Step4:Hello World Again,{}".format(get_current_time()))
    requests_get('http://dreamtown.synology.me:5184', headers)
    logger.info("\n")

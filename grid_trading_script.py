from utils import *

if __name__ == "__main__":
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNDY4ODY3OTlAMTYzLmNvbSIsImV4cGlyZXMiOjE3NTM1MjI2NjYuMTE3MDQ2fQ.yIeNVqU_A45hkRlLvbZ9QK82DUY_6g7E2DsOB2M8VU4',
        'Content-Type': 'application/json',
    }
    logger.info("***Step1:Hello World,{}".format(get_current_time()))
    requests_get('http://dreamtown.synology.me:5181', headers)
    logger.info("\n")

    logger.info("***Step2:Download Data")
    download_data = {
        "start_date": "2023-08-21",
        "end_date": "2030-12-31",
        "source": "akshare_stock",
        "freq": "1d"
    }
    requests_post('http://dreamtown.synology.me:5181/grid/data', headers, download_data)
    logger.info("\n")

    logger.info("***Step3:Generate Signals：艾融软件")
    signal_data = {
          "start_date": "2023-08-21",
          "end_date": "2030-12-31",
          "backtest_config": "grid_arrj_1d",
          "stock_abbr": "arrj",
          "strategy_name": "trend_following",
          "grid_low": 6.25,
          "grid_high": 10.35,
          "grid_num": 6
    }
    requests_post('http://dreamtown.synology.me:5181/grid/signals', headers, signal_data)
    logger.info("\n")

    logger.info("***Step3:Generate Signals：长江电力")
    signal_data = {
          "start_date": "2023-08-21",
          "end_date": "2030-12-31",
          "backtest_config": "grid_cjdl_1d",
          "stock_abbr": "cjdl",
          "strategy_name": "trend_following",
          "grid_low": 6.25,
          "grid_high": 10.35,
          "grid_num": 6
    }
    requests_post('http://dreamtown.synology.me:5181/grid/signals', headers, signal_data)
    logger.info("\n")

    logger.info("***Step3:Generate Signals：招商银行")
    signal_data = {
          "start_date": "2023-08-21",
          "end_date": "2030-12-31",
          "backtest_config": "grid_zsyh_1d",
          "stock_abbr": "zsyh",
          "strategy_name": "trend_following",
          "grid_low": 6.25,
          "grid_high": 10.35,
          "grid_num": 6
    }
    requests_post('http://dreamtown.synology.me:5181/grid/signals', headers, signal_data)
    logger.info("\n")

    logger.info("***Step3:Generate Signals：美的集团")
    signal_data = {
          "start_date": "2023-08-21",
          "end_date": "2030-12-31",
          "backtest_config": "grid_mdjt_1d",
          "stock_abbr": "mdjt",
          "strategy_name": "trend_following",
          "grid_low": 6.25,
          "grid_high": 10.35,
          "grid_num": 6
    }
    requests_post('http://dreamtown.synology.me:5181/grid/signals', headers, signal_data)
    logger.info("\n")

    logger.info("***Step3:Generate Signals：软通动力")
    signal_data = {
          "start_date": "2023-08-21",
          "end_date": "2030-12-31",
          "backtest_config": "grid_rtdl_1d",
          "stock_abbr": "rtdl",
          "strategy_name": "trend_following",
          "grid_low": 6.25,
          "grid_high": 10.35,
          "grid_num": 6
    }
    requests_post('http://dreamtown.synology.me:5181/grid/signals', headers, signal_data)
    logger.info("\n")

    logger.info("***Step3:Generate Signals：海康威视")
    signal_data = {
          "start_date": "2023-08-21",
          "end_date": "2030-12-31",
          "backtest_config": "grid_hkws_1d",
          "stock_abbr": "hkws",
          "strategy_name": "trend_following",
          "grid_low": 6.25,
          "grid_high": 10.35,
          "grid_num": 6
    }
    requests_post('http://dreamtown.synology.me:5181/grid/signals', headers, signal_data)
    logger.info("\n")

    logger.info("***Step4:Hello World Again,{}".format(get_current_time()))
    requests_get('http://dreamtown.synology.me:5181', headers)

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
    requests_get('http://dreamtown.synology.me:5181', headers)
    logger.info("\n")

    time.sleep(1)

    logger.info("***Step2:Download Data,{}".format(get_current_time()))
    download_data = {
        "start_date": "2023-08-21",
        "end_date": "2030-12-31",
        "source": "zhitu_stock",
        "freq": "1d",
        "refresh_all": True,
        "market_type": "ZH"
    }
    requests_post('http://dreamtown.synology.me:5181/grid/data', headers, download_data)
    logger.info("\n")

    time.sleep(1)

    logger.info("***Step3:Generate Signals：美的集团,{}".format(get_current_time()))
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

    logger.info("***Step3:Generate Signals：云南白药,{}".format(get_current_time()))
    signal_data = {
          "start_date": "2023-08-21",
          "end_date": "2030-12-31",
          "backtest_config": "grid_ynby_1d",
          "stock_abbr": "ynby",
          "strategy_name": "trend_following",
          "grid_low": 6.25,
          "grid_high": 10.35,
          "grid_num": 6
    }
    requests_post('http://dreamtown.synology.me:5181/grid/signals', headers, signal_data)
    logger.info("\n")

    logger.info("***Step3:Generate Signals：泸州老窖,{}".format(get_current_time()))
    signal_data = {
          "start_date": "2023-08-21",
          "end_date": "2030-12-31",
          "backtest_config": "grid_lzlj_1d",
          "stock_abbr": "lzlj",
          "strategy_name": "trend_following",
          "grid_low": 6.25,
          "grid_high": 10.35,
          "grid_num": 6
    }
    requests_post('http://dreamtown.synology.me:5181/grid/signals', headers, signal_data)
    logger.info("\n")

    logger.info("***Step3:Generate Signals：苏泊尔,{}".format(get_current_time()))
    signal_data = {
          "start_date": "2023-08-21",
          "end_date": "2030-12-31",
          "backtest_config": "grid_sbe_1d",
          "stock_abbr": "sbe",
          "strategy_name": "trend_following",
          "grid_low": 6.25,
          "grid_high": 10.35,
          "grid_num": 6
    }
    requests_post('http://dreamtown.synology.me:5181/grid/signals', headers, signal_data)
    logger.info("\n")

    logger.info("***Step3:Generate Signals：北方华创,{}".format(get_current_time()))
    signal_data = {
          "start_date": "2023-08-21",
          "end_date": "2030-12-31",
          "backtest_config": "grid_bfhc_1d",
          "stock_abbr": "bfhc",
          "strategy_name": "trend_following",
          "grid_low": 6.25,
          "grid_high": 10.35,
          "grid_num": 6
    }
    requests_post('http://dreamtown.synology.me:5181/grid/signals', headers, signal_data)
    logger.info("\n")

    logger.info("***Step3:Generate Signals：软通动力,{}".format(get_current_time()))
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

    logger.info("***Step3:Generate Signals：中国石化,{}".format(get_current_time()))
    signal_data = {
          "start_date": "2023-08-21",
          "end_date": "2030-12-31",
          "backtest_config": "grid_zgsh_1d",
          "stock_abbr": "zgsh",
          "strategy_name": "trend_following",
          "grid_low": 6.25,
          "grid_high": 10.35,
          "grid_num": 6
    }
    requests_post('http://dreamtown.synology.me:5181/grid/signals', headers, signal_data)
    logger.info("\n")

    logger.info("***Step3:Generate Signals：招商银行,{}".format(get_current_time()))
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

    logger.info("***Step3:Generate Signals：恒瑞医药,{}".format(get_current_time()))
    signal_data = {
          "start_date": "2023-08-21",
          "end_date": "2030-12-31",
          "backtest_config": "grid_hryy_1d",
          "stock_abbr": "hryy",
          "strategy_name": "trend_following",
          "grid_low": 6.25,
          "grid_high": 10.35,
          "grid_num": 6
    }
    requests_post('http://dreamtown.synology.me:5181/grid/signals', headers, signal_data)
    logger.info("\n")

    logger.info("***Step3:Generate Signals：长江电力,{}".format(get_current_time()))
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

    time.sleep(3)

    logger.info("***Step3:Generate Signals：五粮液,{}".format(get_current_time()))
    signal_data = {
          "start_date": "2023-08-21",
          "end_date": "2030-12-31",
          "backtest_config": "grid_wly_1d",
          "stock_abbr": "wly",
          "strategy_name": "trend_following",
          "grid_low": 6.25,
          "grid_high": 10.35,
          "grid_num": 6
    }
    requests_post('http://dreamtown.synology.me:5181/grid/signals', headers, signal_data)
    logger.info("\n")
    
    logger.info("***Step3:Generate Signals：福耀玻璃,{}".format(get_current_time()))
    signal_data = {
          "start_date": "2023-08-21",
          "end_date": "2030-12-31",
          "backtest_config": "grid_fybl_1d",
          "stock_abbr": "fybl",
          "strategy_name": "trend_following",
          "grid_low": 6.25,
          "grid_high": 10.35,
          "grid_num": 6
    }
    requests_post('http://dreamtown.synology.me:5181/grid/signals', headers, signal_data)
    logger.info("\n")

    logger.info("***Step3:Generate Signals：伊利股份,{}".format(get_current_time()))
    signal_data = {
          "start_date": "2023-08-21",
          "end_date": "2030-12-31",
          "backtest_config": "grid_ylgf_1d",
          "stock_abbr": "ylgf",
          "strategy_name": "trend_following",
          "grid_low": 6.25,
          "grid_high": 10.35,
          "grid_num": 6
    }
    requests_post('http://dreamtown.synology.me:5181/grid/signals', headers, signal_data)
    logger.info("\n")

    logger.info("***Step3:Generate Signals：工商银行,{}".format(get_current_time()))
    signal_data = {
          "start_date": "2023-08-21",
          "end_date": "2030-12-31",
          "backtest_config": "grid_gsyh_1d",
          "stock_abbr": "gsyh",
          "strategy_name": "trend_following",
          "grid_low": 6.25,
          "grid_high": 10.35,
          "grid_num": 6
    }
    requests_post('http://dreamtown.synology.me:5181/grid/signals', headers, signal_data)
    logger.info("\n")

    logger.info("***Step3:Generate Signals：中国石油,{}".format(get_current_time()))
    signal_data = {
          "start_date": "2023-08-21",
          "end_date": "2030-12-31",
          "backtest_config": "grid_zgsy_1d",
          "stock_abbr": "zgsy",
          "strategy_name": "trend_following",
          "grid_low": 6.25,
          "grid_high": 10.35,
          "grid_num": 6
    }
    requests_post('http://dreamtown.synology.me:5181/grid/signals', headers, signal_data)
    logger.info("\n")

    logger.info("***Step3:Generate Signals：中远海控,{}".format(get_current_time()))
    signal_data = {
          "start_date": "2023-08-21",
          "end_date": "2030-12-31",
          "backtest_config": "grid_zyhk_1d",
          "stock_abbr": "zyhk",
          "strategy_name": "trend_following",
          "grid_low": 6.25,
          "grid_high": 10.35,
          "grid_num": 6
    }
    requests_post('http://dreamtown.synology.me:5181/grid/signals', headers, signal_data)
    logger.info("\n")

    logger.info("***Step3:Generate Signals：韦尔股份,{}".format(get_current_time()))
    signal_data = {
          "start_date": "2023-08-21",
          "end_date": "2030-12-31",
          "backtest_config": "grid_wegf_1d",
          "stock_abbr": "wegf",
          "strategy_name": "trend_following",
          "grid_low": 6.25,
          "grid_high": 10.35,
          "grid_num": 6
    }
    requests_post('http://dreamtown.synology.me:5181/grid/signals', headers, signal_data)
    logger.info("\n")
    
    time.sleep(3)

    logger.info("***Step3:Generate Signals：艾融软件,{}".format(get_current_time()))
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
    # requests_post('http://dreamtown.synology.me:5181/grid/signals', headers, signal_data)
    logger.info("\n")
    
    logger.info("***Step4:Hello World Again,{}".format(get_current_time()))
    requests_get('http://dreamtown.synology.me:5181', headers)
    logger.info("\n")

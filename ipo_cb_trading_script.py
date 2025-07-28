from utils import *

if __name__ == "__main__":
    # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNDY4ODY3OTlAMTYzLmNvbSIsImV4cGlyZXMiOjE3Nzk4Nzc5NjkuNDU3MTM2Mn0.NF1ynVWX_OhXo_UOP-DAc8lyNUDT29_2BCfbQIn8uRc
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNDY4ODY3OTlAMTYzLmNvbSIsImV4cGlyZXMiOjE3Nzk4Nzc5NjkuNDU3MTM2Mn0.NF1ynVWX_OhXo_UOP-DAc8lyNUDT29_2BCfbQIn8uRc',
        'Content-Type': 'application/json',
    }
    base_url = "http://dreamtown.synology.me:8000"
    logger.info("***Step1:Hello World,{}".format(get_current_time()))
    requests_get(base_url, headers)
    logger.info("\n")

    logger.info("***Step2:Download convertible bond IPO Data")
    try:
        requests_get('{}/current_cb_ipo'.format(base_url), headers)
    except Exception as e:  
        logger.error(f"Download convertible bond IPO Data Error: {e}")
    logger.info("\n")

    logger.info("***Step3:Participate convertible bond IPO")
    try:
        requests_get('{}/auto_bond_conv'.format(base_url), headers)
    except Exception as e:
        logger.error(f"Participate convertible bond IPO Error: {e}")
    logger.info("\n")

    logger.info("***Step4:Hello World Again,{}".format(get_current_time()))
    requests_get(base_url, headers)

    import time
    # 暂停 60 秒  
    time.sleep(60) 

from utils import *
import time

if __name__ == "__main__":

    logger.info("永久组合开始")
    content_txt = "{}，交易跟踪：{}，再平衡：{}。".format(get_current_date(),
                                              "https://docs.google.com/spreadsheets/d/181D3VALuL9P3yHlh8tKZDSdH6fuMqUpTE0B5x6NFakM/edit?gid=0#gid=0",
                                              "https://docs.google.com/spreadsheets/d/1Jk7GYXWLAHBjsXZtUMuBtmpE3EWdIDviGOPWKb8hnJs/edit?gid=1843166815#gid=1843166815")
    
    logger.info("***Step1:Bark推送,{}".format(get_current_time()))
    bark_push(title="永久组合",content=content_txt)
    
    time.sleep(1)
    
    logger.info("***Step2:Pushdeer推送,{}".format(get_current_time()))
    pushdeer_push(title="永久组合",content=content_txt)
    logger.info("永久组合结束")

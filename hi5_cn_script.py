from utils import *
import time

if __name__ == "__main__":
    logger.info("A股Hi5跟踪开始")
    content_txt = "{}，A股Hi5跟踪：{}".format(get_current_date(),"https://docs.google.com/spreadsheets/d/1G1E0qtLzt1WulfUk2uSxXrm_HNKejTMwwI-4KF3OG9w/edit?gid=0#gid=0")
    
    logger.info("***Step1:Bark推送,{}".format(get_current_time()))
    bark_push(title="A股Hi5跟踪",content=content_txt)
    
    time.sleep(1)
    
    logger.info("***Step2:Pushdeer推送,{}".format(get_current_time()))
    pushdeer_push(title="A股Hi5跟踪",content=content_txt)
    logger.info("A股Hi5跟踪结束")

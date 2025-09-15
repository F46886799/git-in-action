from utils import *
import time

if __name__ == "__main__":
    logger.info("美股Hi5跟踪开始")
    content_txt = "{}，美股Hi5跟踪：{}".format(get_current_date(),"https://docs.google.com/spreadsheets/d/1G1E0qtLzt1WulfUk2uSxXrm_HNKejTMwwI-4KF3OG9w/edit?gid=0#gid=0")
    bark_push(title="美股Hi5跟踪",content=content_txt)
    time.sleep(1)
    pushdeer_push(title="美股Hi5跟踪",content=content_txt)
    logger.info("美股Hi5跟踪结束")

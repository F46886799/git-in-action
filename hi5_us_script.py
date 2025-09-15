from utils import *
import time

if __name__ == "__main__":
    
    logger.info("美股Hi5跟踪开始")
    content_txt = "{}，请查看：{}".format(today,url)
    bark_push(title="美股Hi5跟踪",content=content_txt)
    time.sleep(1)
    pushdeer_push(title="美股Hi5跟踪",content=content_txt)
    logger.info("美股Hi5跟踪结束")

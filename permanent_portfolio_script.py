from utils import *
import time

if __name__ == "__main__":

    logger.info("【永久组合全球】【王慧玲的汇丰中国】开始")
    content_txt = "{}，交易跟踪：{}，再平衡：{}。".format(get_current_date(),
                                              "https://docs.google.com/spreadsheets/d/181D3VALuL9P3yHlh8tKZDSdH6fuMqUpTE0B5x6NFakM/edit?gid=0#gid=0",
                                              "https://docs.google.com/spreadsheets/d/1Jk7GYXWLAHBjsXZtUMuBtmpE3EWdIDviGOPWKb8hnJs/edit?gid=1843166815#gid=1843166815")
    
    logger.info("***Step1:Bark推送,{}".format(get_current_time()))
    # bark_push(title="【永久组合全球】【王慧玲的汇丰中国】",content=content_txt,category="永久组合全球")
    bark_push_v2(title="【永久组合全球】【王慧玲的汇丰中国】",body=content_txt, group="永久组合全球",
                 icon="https://00.ifreesite.com/world-i/hong_kong_national_emblem.png",
                 url="https://docs.google.com/spreadsheets/d/1G1E0qtLzt1WulfUk2uSxXrm_HNKejTMwwI-4KF3OG9w/edit?gid=0#gid=0")
    
    time.sleep(1)
    
    logger.info("***Step2:Pushdeer推送,{}".format(get_current_time()))
    pushdeer_push(title="【永久组合全球】【王慧玲的汇丰中国】",content=content_txt)
    logger.info("【永久组合全球】【王慧玲的汇丰中国】结束")

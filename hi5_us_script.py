from utils import *
import time

if __name__ == "__main__":
    logger.info("【全天候组合美股】【张甫的华泰国际】开始")

    crashed = target_crash(ticker="RSP.US")

    if crashed:
        content_txt = "{}，跟踪ETF（RSP.US）的状态【跌幅已超过1%，需要开仓】。交易跟踪：{}；再平衡：{}；原始跟踪：{}。".format(get_current_date(),"https://docs.google.com/spreadsheets/d/1uWR55sm4PoAZSG6KRh4T2guF91bdPaVcEQfis2p_tY8/edit?gid=0#gid=0","https://docs.google.com/spreadsheets/d/1g96AXTEuqP0uZbBhH6HkK1ayqK5nh2srQvgC4Gu6E4I/edit?gid=1843166815#gid=1843166815","https://docs.google.com/spreadsheets/d/1G1E0qtLzt1WulfUk2uSxXrm_HNKejTMwwI-4KF3OG9w/edit?gid=0#gid=0")
    else:
        content_txt = "{}，跟踪ETF（RSP.US）的状态【正常，无需开仓】。交易跟踪：{}；再平衡：{}；原始跟踪：{}。".format(get_current_date(),"https://docs.google.com/spreadsheets/d/1uWR55sm4PoAZSG6KRh4T2guF91bdPaVcEQfis2p_tY8/edit?gid=0#gid=0","https://docs.google.com/spreadsheets/d/1g96AXTEuqP0uZbBhH6HkK1ayqK5nh2srQvgC4Gu6E4I/edit?gid=1843166815#gid=1843166815","https://docs.google.com/spreadsheets/d/1G1E0qtLzt1WulfUk2uSxXrm_HNKejTMwwI-4KF3OG9w/edit?gid=0#gid=0")
    
    logger.info("***Step1:Bark推送,{}".format(get_current_time()))
    bark_push_v2(title="【全天候组合美股】【张甫的华泰国际】",body=content_txt, group="全天候组合美股",
                 icon="https://00.ifreesite.com/world-i/united_states_of_america_national_emblem.png",
                 url="https://docs.google.com/spreadsheets/d/1G1E0qtLzt1WulfUk2uSxXrm_HNKejTMwwI-4KF3OG9w/edit?gid=0#gid=0")
    
    time.sleep(1)
    
    logger.info("***Step2:Pushdeer推送,{}".format(get_current_time()))
    pushdeer_push(title="【全天候组合美股】【张甫的华泰国际】",content=content_txt)
    logger.info("【全天候组合美股】【张甫的华泰国际】结束")

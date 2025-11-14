from utils import *
import time

if __name__ == "__main__":

    logger.info("【全天候组合A股】【张甫的国君普通】开始")
    content_txt = "{}，交易跟踪：{}，再平衡：{}。".format(get_current_date(),
                                              "https://docs.google.com/spreadsheets/d/19dkG30h9jeVHrF5O_ugqwflmfdUItm6FSMccM_igRnc/edit?gid=0#gid=0",
                                              "https://docs.google.com/spreadsheets/d/16WjXzYSZgrJNy6YgNgwJvB3JdLhhmbe-A9rlohLWmwg/edit?gid=1843166815#gid=1843166815")
    
    logger.info("***Step1:Bark推送,{}".format(get_current_time()))
    # bark_push(title="【全天候组合A股】【张甫的国君普通】",content=content_txt,category="全天候组合A股")
    bark_push_v2(title="【全天候组合A股】【张甫的国君普通】",body=content_txt, group="全天候组合A股",
                 icon="https://00.ifreesite.com/world-i/chian_national_emblem.png",
                 url="https://docs.google.com/spreadsheets/d/1G1E0qtLzt1WulfUk2uSxXrm_HNKejTMwwI-4KF3OG9w/edit?gid=0#gid=0")
    
    time.sleep(1)
    
    logger.info("***Step2:Pushdeer推送,{}".format(get_current_time()))
    pushdeer_push(title="【全天候组合A股】【张甫的国君普通】",content=content_txt)
    logger.info("【全天候组合A股】【张甫的国君普通】结束")

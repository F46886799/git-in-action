from utils import *
import time

if __name__ == "__main__":

    logger.info("【全天候组合A股】【张甫的国君普通】开始")
    content_txt = "{}，交易跟踪：{}，再平衡：{}。".format(get_current_date(),
                                              "https://docs.google.com/spreadsheets/d/19dkG30h9jeVHrF5O_ugqwflmfdUItm6FSMccM_igRnc/edit?gid=0#gid=0",
                                              "https://docs.google.com/spreadsheets/d/16WjXzYSZgrJNy6YgNgwJvB3JdLhhmbe-A9rlohLWmwg/edit?gid=1843166815#gid=1843166815")
    
    logger.info("***Step1:Bark推送,{}".format(get_current_time()))
    bark_push(title="【全天候组合A股】【张甫的国君普通】",content=content_txt,category="全天候组合A股")
    
    time.sleep(1)
    
    logger.info("***Step2:Pushdeer推送,{}".format(get_current_time()))
    pushdeer_push(title="【全天候组合A股】【张甫的国君普通】",content=content_txt)
    logger.info("【全天候组合A股】【张甫的国君普通】结束")

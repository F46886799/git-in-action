from datetime import datetime as dt
from pytz import timezone
import requests
from loguru import logger
from BarkNotificator import BarkNotificator
from pypushdeer import PushDeer


def bark_push（title="welcome", content="hello world"）：
    bark = BarkNotificator(device_token="your device token")
    bark.send(title=title, content=content)


def pushdeer_push（title="# hello world", content="**optional** description in markdown"）：
    pushdeer = PushDeer(pushkey="your_push_key")
    pushdeer.send_markdown(title, desp=content)


def get_current_time(tz: str = "Asia/Shanghai", time_format: str = "%Y-%m-%d %H:%M:%S"):
    current_time = dt.now(timezone(tz)).strftime(time_format)
    return current_time


def get_current_date(tz: str = "Asia/Shanghai", date_format: str = "%Y-%m-%d"):
    current_date = dt.now(timezone(tz)).strftime(date_format)
    return current_date


def requests_get(url: str, headers=None, params=None):
    # 发送 GET 请求，连接超时30秒，响应超时60*60*4秒，即4个小时
    if params is None:
        response = requests.get(url, headers=headers, timeout=(60*5, 60 * 60 * 4))
    else:
        response = requests.get(url, params=params, headers=headers, timeout=(60*5, 60 * 60 * 4))
    # 检查响应状态
    if response.status_code == 200:
        logger.info("请求成功!")
        # 输出响应内容
        logger.info(response.json())  # 将响应内容解析为 JSON
    else:
        logger.info("请求失败:", response.status_code)


def requests_post(url: str, headers=None, data=None):
    # 发送 POST 请求，连接超时30秒，响应超时60*60*4秒，即4个小时
    response = requests.post(url, headers=headers, json=data, timeout=(60*5, 60 * 60 * 4))

    # 检查响应状态
    if response.status_code == 200:
        logger.info("数据已创建!")
        logger.info(response.json())
    else:
        logger.info("请求失败:", response.status_code)

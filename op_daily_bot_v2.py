import requests
import json
from datetime import datetime
from zoneinfo import ZoneInfo

# 配置部分
URL = "http://bird5gw.i2soft.net/plugins/plugins/srvcStatus/qryBatchUpdStatus?operKey=2b20f5cf398c4bd0b28113c57ebcac6c"
# 测试URL
# https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=d0b61849-a811-419a-92b8-2c7147fc6ba7
# 员工关系URL
# https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=550fcfea-c715-4a6f-9e8f-5efdbad7c279
WEIXIN_YUANGONG_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=d0b61849-a811-419a-92b8-2c7147fc6ba7"
WEIXIN_PLATFORM_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=550fcfea-c715-4a6f-9e8f-5efdbad7c279"
# 定义报告模版
REPORT_TEMPLATE_ORIG = """四中心，{date} 运营早报
一、服务节点：
1. 运行中：{[D]运行中_count}
2. 8点半前迟到：{[A]中断(无签到/无请假/未审批/非退场/8点半前)_count}，（人员清单：{[A]中断(无签到/无请假/未审批/非退场/8点半前)_empName}）
3. 8点半~9点迟到：{[A]中断(无签到/无请假/未审批/非退场/8点半前)_count}，（人员清单：{[A]中断(无签到/无请假/未审批/非退场/8点半前)_empName}）
4. 9点后迟到：{[A]中断(无签到/无请假/未审批/非退场/8点半前)_count}，（人员清单：{[A]中断(无签到/无请假/未审批/非退场/8点半前)_empName}）
5. 待岗人数：{[B]终止(待岗)_count}，（人员清单：{[B]终止(待岗)_empName}）
6. 离职人数：{[A]中断(离职中)_count}，（人员清单：{[A]中断(离职中)_empName}）
7. 待上岗人数：{[C]Idle(已入职待上岗)_count}，（人员清单：{[C]Idle(已入职待上岗)_empName}）

二、订单指标：
1. 进行中需求订单：{ordersDetail_ordersNum}
2. 进行中招聘订单：{ordersDetail_jobNum}

三、积压任务：
1. 超10天积压任务数：{statFlowData_count}"""


REPORT_TEMPLATE = """
## 四中心运营早报，{date}，{date_str}
### <font color="info">一、服务节点：</font>
1. 总人数：{total_count}
2. 运行中人数：{d41bee83a766f44158476c7a006e127d}
<font color="warning">3. 8点半前迟到：{dcac5153426d4b7eb38a36a1094f35f0}，（人员清单：{02425d600527b781c647f14dde84b9aa}）</font>
<font color="warning">4. 8点半~9点迟到：{a487e6c867b5ff606dab82c1c79f4ec7}，（人员清单：{be8130f258c7798bebf5dfa428f21f12}）</font>
<font color="warning">5. 9点后迟到：{fa070fc658b879f64596348c68fead5b}，（人员清单：{a04b00a74238772e0785ce8efda36725}）</font>
6. 待岗中人数：{264ef56922629f76a107c32853621ef1}，（人员清单：{7eb8e3ba20f450353355a170431b6860}）
7. 离职中人数：{3df42d9589645c0480186ce2876c0822}，（人员清单：{928e5e3246ee01f62d8f17482a8052ac}）
8. 待上岗人数：{a02a7a14dd328d57639e4a5953b86b74}，（人员清单：{901247dd5966f0d35ebbc3575325bb37}）
### <font color="info">二、订单指标：</font>
1. 进行中需求订单：{ordersDetail_ordersNum}
2. 进行中招聘订单：{ordersDetail_jobNum}
3. 有简历招聘订单：{ordersDetail_hasResumeNum}
4. 无简历招聘订单：{ordersDetail_nullResumeNum}
### <font color="info">三、积压任务：</font>
<font color="warning">1. 超10天积压任务数：{statFlowData_count}</font>
<font color="warning">2. 超10天积压任务明细：{statFlowData_fd_str}</font>
"""

import hashlib

def md5_string(text):
    # 创建md5对象
    md5 = hashlib.md5()
    # 更新哈希对象，需要将字符串编码为字节
    md5.update(text.encode('utf-8'))
    # 返回十六进制格式的哈希值
    md5_text = md5.hexdigest()
    print("---------start")
    print(text)
    print(md5_text)
    print("---------end")
    return md5_text


def get_api_data(url):
    """请求 API 并返回 JSON 数据"""
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"请求接口出错: {e}")
        return None

def format_person_list(person_list):
    """辅助函数：将列表转换为字符串，如果是 None 则返回 '无'"""
    if not person_list:
        return "无"
    if isinstance(person_list, list):
        return "、".join([str(p) for p in person_list])
    return str(person_list)

def parse_and_map_data(json_data):
    """
    核心步骤：将 API 返回的 JSON 字段映射到模版需要的变量
    注意：这里的 .get('key') 中的 key 需要替换为你实际 API 返回的字段名
    """
    
    # 获取当天的日期
    tz = ZoneInfo('Asia/Shanghai')
    today_str = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    day_index = datetime.now(tz).weekday()  
    date_str = weekdays[day_index]
    
    # --- 关键修改区域 START ---
    # 请根据 print(json_data) 打印出的实际结构，修改下方的 get 参数
    # 假设 API 返回的结构是扁平的，或者你需要从嵌套结构中提取

    mapping = {
        "date": today_str,
        "date_str": date_str
    }
    # --- 关键修改区域 END ---

    # 服务状态
    total_count = 0
    all_srvcStatus = json_data.get("srvcStatus")
    for srvcStatus in all_srvcStatus:
        item_srvcStatus_name = srvcStatus.get("srvcStatus","状态未明")
        item_srvcStatus_empName = srvcStatus.get("empName","无")
        item_srvcStatus_count = srvcStatus.get("count",0)
        item_srvcStatus_operDeptName = srvcStatus.get("operDeptName","四中心")
        mapping[md5_string(item_srvcStatus_name+"_status")] = item_srvcStatus_name
        mapping[md5_string(item_srvcStatus_name+"_empName")] = item_srvcStatus_empName
        mapping[md5_string(item_srvcStatus_name+"_count")] = item_srvcStatus_count
        mapping[md5_string(item_srvcStatus_name+"_operDeptName")] = item_srvcStatus_operDeptName
        total_count +=item_srvcStatus_count
    mapping["total_count"] = total_count

    if md5_string("[A]中断(无签到/无请假/未审批/非退场/8点半前)_count") not in mapping:
        mapping[md5_string("[A]中断(无签到/无请假/未审批/非退场/8点半前)_count")] = 0
        mapping[md5_string("[A]中断(无签到/无请假/未审批/非退场/8点半前)_empName")] = "无"
    if md5_string("[A]中断(无签到/无请假/未审批/非退场/9点前)_count") not in mapping:
        mapping[md5_string("[A]中断(无签到/无请假/未审批/非退场/9点前)_count")] = 0
        mapping[md5_string("[A]中断(无签到/无请假/未审批/非退场/9点前)_empName")] = "无"
    if md5_string("[A]中断(无签到/无请假/未审批/非退场/9点后)_count") not in mapping:
        mapping[md5_string("[A]中断(无签到/无请假/未审批/非退场/9点后)_count")] = 0
        mapping[md5_string("[A]中断(无签到/无请假/未审批/非退场/9点后)_empName")] = "无"

    # 订单情况
    ordersDetail_jobNum = json_data.get("ordersDetail").get("jobNum",0)
    mapping["ordersDetail_jobNum"] = ordersDetail_jobNum
    ordersDetail_ordersNum = json_data.get("ordersDetail").get("ordersNum",0)
    mapping["ordersDetail_ordersNum"] = ordersDetail_ordersNum
    ordersDetail_jobChgNum = json_data.get("ordersDetail").get("jobChgNum",0)
    mapping["ordersDetail_jobChgNum"] = ordersDetail_jobChgNum
    ordersDetail_hasResumeNum = json_data.get("ordersDetail").get("hasResumeNum",0)
    mapping["ordersDetail_hasResumeNum"] = ordersDetail_hasResumeNum
    ordersDetail_nullResumeNum = json_data.get("ordersDetail").get("nullResumeNum",0)
    mapping["ordersDetail_nullResumeNum"] = ordersDetail_nullResumeNum

     # 风险节点
    riskNode_count = json_data.get("riskNode").get("count",0)
    mapping["riskNode_count"] = riskNode_count
    riskNode_empName = json_data.get("riskNode").get("empName","无")
    mapping["riskNode_empName"] = riskNode_empName

    # 待办任务
    statFlowData_flowDetail = json_data.get("statFlowData").get("flowDetail")

    statFlowData_fd_str = ""
    for statFlowData_fd in statFlowData_flowDetail:
        statFlowData_fd_str += "【" + statFlowData_fd["flowName"] + ","
        statFlowData_fd_str += statFlowData_fd["dscr"] + ","
        statFlowData_fd_str += statFlowData_fd["dealerName"] + ","
        statFlowData_fd_str += str(statFlowData_fd["duration"]) + "】"
    mapping["statFlowData_fd_str"] = statFlowData_fd_str

    statFlowData_count = json_data.get("statFlowData").get("count",0) 
    mapping["statFlowData_count"] = statFlowData_count

    return mapping

def main():

    tz = ZoneInfo('Asia/Shanghai')
    today_date_str = datetime.now(tz).strftime("%Y-%m-%d")
    is_work_day = work_day(today_date_str)

    if not is_work_day:
        print("当前日期不是工作日，直接退出...")
        return    

    print("正在获取数据...")
    raw_data = get_api_data(URL)
    
    if raw_data:
        # 打印原始数据，方便你调试和查看真实的字段名
        print("\n--- API 返回的原始数据 (用于对照字段名) ---")
        print(json.dumps(raw_data, indent=4, ensure_ascii=False))
        print("------------------------------------------\n")

        # 处理数据
        try:
            context = parse_and_map_data(raw_data)
            
            # 生成报告
            final_report = REPORT_TEMPLATE.format(**context)
            
            print("--- 生成的早报内容 ---")
            print(final_report)

            # 初始化
            send_work_weixin_markdown_msg(WEIXIN_YUANGONG_URL,final_report)
            # 迟到提醒HRBP
            send_work_weixin_msg(WEIXIN_YUANGONG_URL,daily_checkin_msg)
            # 积压任务提醒所有
            send_work_weixin_msg(WEIXIN_YUANGONG_URL,all_msg)
            # 积压任务提醒所有
            # send_work_weixin_msg(WEIXIN_YUANGONG_URL,template_card_msg)
            
        except KeyError as e:
            print(f"数据解析错误，模版中缺少对应的字段数据: {e}")
    else:
        print("无法获取数据，生成失败。")


def send_work_weixin_markdown_msg(webhook, msg):
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": msg
        }
    }
    res = requests.post(webhook, json=data).json()
    if res["errcode"] != 0:
        print(f"发送企业微信群markdown消息失败：{res['errmsg']}")
    print(f"发送企业微信群markdown消息成功")

# "15201136765" 王洪涛
# "18516995417" 王跃山
# "15266263350" 张雪莹
# "18611331816" 蒋洁

template_card_msg = {
    "msgtype":"template_card",
    "template_card":{
        "card_type":"text_notice",
        "source":{
            "icon_url":"https://wework.qpic.cn/wwpic/252813_jOfDHtcISzuodLa_1629280209/0",
            "desc":"企业微信",
            "desc_color":0
        },
        "main_title":{
            "title":"欢迎使用企业微信",
            "desc":"您的好友正在邀请您加入企业微信"
        },
        "emphasis_content":{
            "title":"100",
            "desc":"数据含义"
        },
        
        "sub_title_text":"下载企业微信还能抢红包！",
        "horizontal_content_list":[
            {
                "keyname":"邀请人",
                "value":"张三"
            },
            {
                "keyname":"企微官网",
                "value":"点击访问",
                "type":1,
                "url":"https://work.weixin.qq.com/?from=openApi"
            },
            {
                "keyname":"企微下载",
                "value":"企业微信.apk",
                "type":2,
                "media_id":"MEDIAID"
            }
        ]
    }
}

daily_checkin_msg = {
        "msgtype": "text",
        "text": {
            "content": "请跟进运营早报中的迟到情况，并于当日上午10点15分前反馈具体原因。",
            "mentioned_mobile_list":["15201136765","@all"]
        }
    }

all_msg = {
        "msgtype": "text",
        "text": {
            "content": "请各位关注运营早报中的理积压任务，周五下班前完成积压任务处理。",
            "mentioned_mobile_list":["18516995417","@all"]
        }
    }

def send_work_weixin_msg(webhook, msg):
    res = requests.post(webhook, json=msg).json()
    if res["errcode"] != 0:
        print(f"发送企业微信群文本消息失败：{res['errmsg']}")
    print(f"发送企业微信群文本消息成功")


def work_day(now_date):

    # 1566-节假日安排查询 - 代码参考（根据实际业务情况修改）

    # 基本参数配置
    apiUrl = 'http://apis.juhe.cn/fapig/calendar/day'  # 接口请求URL
    apiKey = 'e06a9be9f7734f143ecdb79ddacc4c0c'  # 在个人中心->我的数据,接口名称上方查看

    # 接口请求入参配置
    requestParams = {
        'key': apiKey,
        'date': now_date,
        'detail': '',
    }

    # 发起接口网络请求
    response = requests.get(apiUrl, params=requestParams)

    # 解析响应结果
    if response.status_code == 200:
        responseResult = response.json()
        # 网络请求成功。可依据业务逻辑和接口文档说明自行处理。
        print(responseResult)
        # {
        #     "reason": "success",
        #     "result": {
        #         "date": "2026-02-12",
        #         "week": "星期四",
        #         "statusDesc": "工作日",
        #         "status": null
        #     },
        #     "error_code": 0
        # }
        if responseResult["result"]["statusDesc"] == '工作日':
            return True
        else:
            return False
    else:
        # 网络异常等因素，解析结果异常。可依据业务逻辑自行处理。
        print('请求异常')
        return False
    

if __name__ == "__main__":
    main()

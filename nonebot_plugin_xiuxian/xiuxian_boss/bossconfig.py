import json
import os
from pathlib import Path

configkey = ["Boss灵石", "Boss名字", "Boss倍率", "Boss个数上限", "Boss生成时间参数", 'open', "世界积分商品"]
CONFIG = {
    "open":[],
    "Boss灵石" : {
    #生成Boss给的灵石
    '练气境':5000,
    '筑基境':10000,
    '结丹境':20000,
    '元婴境':30000,
    '化神境':60000,
    '炼虚境':120000,
    '合体境':240000,
    '大乘境':800000,
    '渡劫境':1800000,
    '真仙境':4000000,
    '金仙境':10000000,
    '太乙境':30000000,
    },
    "Boss名字":["墨蛟","婴鲤兽","千目妖","鸡冠蛟","妖冠蛇","铁火蚁","天晶蚁","银光鼠","紫云鹰","狗青"],#生成的Boss名字，自行修改
    "Boss个数上限":10,
    "Boss倍率":{
        #Boss属性：大境界平均修为是基础数值，气血：15倍，真元：10倍，攻击力：0.2倍
        #作为参考：人物的属性，修为是基础数值，气血：0.5倍，真元：1倍，攻击力：0.1倍
        "气血":100,
        "真元":10,
        "攻击":0.2
    },
    "Boss生成时间参数":{#Boss生成的时间，每1小时5分钟生成一只，2个不可全为0
        "hours":1,
        "minutes":0
    },
    "世界积分商品":{
        "1":{
            "id":1999,
            "cost":1000,
            "desc":"渡厄丹，使下一次突破丢失的修为减少为0！"
        },
        "2":{
            "id":4003,
            "cost":1000,
            "desc":"陨铁炉，以陨铁炼制的丹炉，耐高温，具有基础的炼丹功能"
        },
        "3":{
            "id":4002,
            "cost":5000,
            "desc":"雕花紫铜炉，表面刻有精美雕花的紫铜丹炉，一看便出自大师之手，可以使产出的丹药增加1枚"
        },
        "4":{
            "id":4001,
            "cost":20000,
            "desc":"寒铁铸心炉，由万年寒铁打造的顶尖丹炉，可以使产出的丹药增加2枚"
        },
        "5":{
            "id":2500,
            "cost":1000,
            "desc":"一级聚灵旗，提升洞天福地中的灵气汇集速度，加速修炼速度和灵田中药材生长速度"
        },
        "6":{
            "id":2501,
            "cost":2000,
            "desc":"二级聚灵旗，提升洞天福地中的灵气汇集速度，加速修炼速度和灵田中药材生长速度"
        },
        "7":{
            "id":2502,
            "cost":4000,
            "desc":"三级聚灵旗，提升洞天福地中的灵气汇集速度，加速修炼速度和灵田中药材生长速度"
        },
        "8":{
            "id":2503,
            "cost":8000,
            "desc":"四级聚灵旗，提升洞天福地中的灵气汇集速度，加速修炼速度和灵田中药材生长速度"
        },
        "9":{
            "id":2504,
            "cost":16000,
            "desc":"仙级聚灵旗，大幅提升洞天福地中的灵气汇集速度，加速修炼速度和灵田中药材生长速度"
        },
    }
}

def get_config():
    try:
        config = readf()
        for key in configkey:
            if key not in list(config.keys()):
                config[key] = CONFIG[key]
        savef(config)
    except:
        config = CONFIG
        savef(config)
    return config

CONFIGJSONPATH = Path(__file__).parent
FILEPATH = CONFIGJSONPATH / 'config.json'
def readf():
    with open(FILEPATH, "r", encoding="UTF-8") as f:
        data = f.read()
    return json.loads(data)


def savef(data):
    data = json.dumps(data, ensure_ascii=False, indent=3)
    savemode = "w" if os.path.exists(FILEPATH) else "x"
    with open(FILEPATH, mode=savemode, encoding="UTF-8") as f:
        f.write(data)
        f.close
    return True

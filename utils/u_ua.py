#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2024-04-29 10:06
# describe：
from random_useragent import UserAgent


# 第三方随机 UserAgent 的对象：pip install r-useragent
r_user_agent_obj: UserAgent = None


def get_r_user_agent():
    global r_user_agent_obj
    r_user_agent_obj = r_user_agent_obj or UserAgent()
    return r_user_agent_obj


def random_one() -> str:
    """
    随机获取一个 user_agent
    :return:
    """
    return get_r_user_agent().random()

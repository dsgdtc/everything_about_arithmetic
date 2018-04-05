#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: mlbdz迷离傍地走.py
Author: dsgdtc@163.com
Date: 2018/1/4 17:37
甘特图
算法：
贪心
所有事件中的最短时间为B[1]，1小时，由于B[1]在第二阶段，则将其最后执行
次短时间是A[2]，2小时，由于A[2]在第一阶段，则将其优先执行
"""

import pprint
import copy

def find_shortest_time(event_1, event_2):

    # 好像用dataframe更好实现

    tmp = event_1[0]["using_time"]
    event_1_min = event_1[0]
    for item in event_1:
        if item["using_time"] < tmp:
            tmp = item["using_time"]
            event_1_min = item


    tmp = event_2[0]["using_time"]
    event_2_min = event_2[0]
    for item in event_2:
        if item["using_time"] < tmp:
            tmp = item["using_time"]
            event_2_min = item

    # print (event_1_min, event_2_min)
    if event_1_min["using_time"] < event_2_min["using_time"]:
        return event_1_min
    else:
        return event_2_min
    # if min(event_1) < min(event_2):
    #     min_index = event_1_min_index
    #     shortest_time = min(event_1)
    #     locate = "event_1"
    # else:
    #     min_index = event_2_min_index
    #     shortest_time = min(event_2)
    #     locate = "event_2"


    # return locate, shortest_time, min_index
    return None

def gantt_chart(event_1, event_2):

    # 整理数据,我想要的结果是每个数据带上自己所在的阶段以及所在阶段的索引位置
    # [["event_1", 8, 0], ["event_1", 6, 1], ["event_1", 2, 2], ["event_1", 4, 3]]
    # [所在阶段, 索引位置, 消耗时间]
    extend_event_1 = []
    for i in range(len(event_1)):
        extend_event_1.append({
            "stage":"event_1",
            "index":i,
            "using_time": event_1[i]})

    extend_event_2 = []
    for i in range(len(event_2)):
        extend_event_2.append({
            "stage":"event_2",
            "index":i,
            "using_time": event_2[i]})

    print ("整理后的数据结构:[索引位置, 所在阶段, 任务消耗时间]")
    pprint.pprint(extend_event_1)
    pprint.pprint(extend_event_2)

    event_1_sort = []
    event_2_sort = []
    # while len(event_1) > 0:
    for i in range(len(event_1)):
        event_min = find_shortest_time(extend_event_1, extend_event_2)
        print ("整个任务中消耗时间最短的是%s" %(event_min))
        if event_min["stage"] == "event_2":
            print("事件%s在2阶段,最后执行" % (event_min))
            event_2_sort.append(copy.deepcopy(event_min))
        else:
            print("事件%s在1阶段,优先执行" % (event_min))
            event_1_sort.append(copy.deepcopy(event_min))

        input("enter to continue...")
        # 假装删除掉,如果真的del这个值，索引不好找
        extend_event_1[event_min["index"]]["using_time"] = 9999
        extend_event_2[event_min["index"]]["using_time"] = 9999

    event_1_sort = event_1_sort
    event_2_sort.reverse()

    result = event_1_sort + event_2_sort
    name_map = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
    }
    print ("事件执行顺序:")
    for item in result:
        print (name_map[item["index"]])


if __name__ == "__main__":

    event_1 = [8, 6, 2, 4]
    event_2 = [3, 1, 3, 12]
    gantt_chart(event_1, event_2)
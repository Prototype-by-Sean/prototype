# -*- coding: utf-8 -*-

# ========從資料庫撈取符合對象=========可同時輸入多筆代號   結果會疊加  ex: find_q_set(1,4) 結果為 [異性男] 跟 [異性女] 集合


def find_q_set(model, *args):
    q_set = {}
    q_set_temp = None
    for c in args:
        # ========篩選需求=========
        if c == 1:
            q_set_temp = model.objects.filter(biological_sex__biological_sex='男', sexuality__sexuality='異性').values()
        elif c == 2:
            q_set_temp = model.objects.filter(biological_sex__biological_sex='男', sexuality__sexuality='同性').values()
        elif c == 3:
            q_set_temp = model.objects.filter(biological_sex__biological_sex='男', sexuality__sexuality='雙性').values()
        elif c == 4:
            q_set_temp = model.objects.filter(biological_sex__biological_sex='女', sexuality__sexuality='異性').values()
        elif c == 5:
            q_set_temp = model.objects.filter(biological_sex__biological_sex='女', sexuality__sexuality='同性').values()
        elif c == 6:
            q_set_temp = model.objects.filter(biological_sex__biological_sex='女', sexuality__sexuality='雙性').values()
        # ========篩選需求=========

        # ========寫入結果=========
        for c1 in q_set_temp:
            c2 = str(c1['id'])
            q_set[c2] = 0
        # ========寫入結果=========
    return q_set


# 範圍性過濾器,輸入model,優先權字典,最大最小值,結果為新的優先權字典


def filter_age(model, q_set, *args):
    # qs_set  為一個優先權字典 {'id1' : 2, 'id2' : 1.....
    # args  為年齡上下限
    args = sorted(args)
    q_set_out = {}
    for c in q_set:
        if model.objects.get(id=int(c)).age in range(args[0], args[1]+1):
            q_set_out[c] = q_set[c] + 1
        else:
            q_set_out[c] = q_set[c]
    return q_set_out


def filter_weight(model, q_set, *args):
    # qs_set  為一個優先權字典 {'id1' : 2, 'id2' : 1.....
    # args  為體重上下限
    args = sorted(args)
    q_set_out = {}
    for c in q_set:
        if model.objects.get(id=int(c)).weight in range(args[0], args[1]+1):
            q_set_out[c] = q_set[c] + 1
        else:
            q_set_out[c] = q_set[c]
    return q_set_out


def filter_height(model, q_set, *args):
    # qs_set  為一個優先權字典 {'id1' : 2, 'id2' : 1.....
    # args  為身高上下限
    args = sorted(args)
    q_set_out = {}
    for c in q_set:
        if model.objects.get(id=int(c)).height in range(args[0], args[1]+1):
            q_set_out[c] = q_set[c] + 1
        else:
            q_set_out[c] = q_set[c]
    return q_set_out


def filter_blood_type(model, q_set, blood_type_list):
    q_set_out = {}
    for c in q_set:
        if model.objects.get(id=int(c)).blood_type_id in blood_type_list:
            q_set_out[c] = q_set[c] + 1
        else:
            q_set_out[c] = q_set[c]
    return q_set_out

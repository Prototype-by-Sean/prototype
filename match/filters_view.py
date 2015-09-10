# -*- coding: utf-8 -*-


def find_q_set(model,*args):
    q_set = []
    q_set_temp = []
    for c in args:
        # ========篩選需求=========
        if c == 1:
            q_set_temp = model.objects.filter(biological_sex='男', sexuality='異性')
        elif c == 2:
            q_set_temp = model.objects.filter(biological_sex='男', sexuality='同性')
        elif c == 3:
            q_set_temp = model.objects.filter(biological_sex='男', sexuality='雙性')
        elif c == 4:
            q_set_temp = model.objects.filter(biological_sex='女', sexuality='異性')
        elif c == 5:
            q_set_temp = model.objects.filter(biological_sex='女', sexuality='同性')
        elif c == 6:
            q_set_temp = model.objects.filter(biological_sex='女', sexuality='雙性')
        # ========篩選需求=========

        # ========寫入結果=========
        q_set = q_set + q_set_temp.values()
        # ========寫入結果=========
    return q_set
# ========從資料庫撈取符合對象=========可同時輸入多筆代號   結果會疊加  ex: find_q_set(1,4) 結果為 [異性男] 跟 [異性女] 集合

# -*- coding: utf-8 -*-


def find_q_set(model, *args):
    qs_set = []
    qs_set_temp = None
    for c in args:
        # ========篩選需求=========
        if c == 1:
            qs_set_temp = model.objects.filter(biological_sex__biological_sex='男', sexuality__sexuality='異性')
        elif c == 2:
            qs_set_temp = model.objects.filter(biological_sex__biological_sex='男', sexuality__sexuality='同性')
        elif c == 3:
            qs_set_temp = model.objects.filter(biological_sex__biological_sex='男', sexuality__sexuality='雙性')
        elif c == 4:
            qs_set_temp = model.objects.filter(biological_sex__biological_sex='女', sexuality__sexuality='異性')
        elif c == 5:
            qs_set_temp = model.objects.filter(biological_sex__biological_sex='女', sexuality__sexuality='同性')
        elif c == 6:
            qs_set_temp = model.objects.filter(biological_sex__biological_sex='女', sexuality__sexuality='雙性')
        # ========篩選需求=========

        # ========寫入結果=========
        for c1 in range(len(qs_set_temp)):
            qs_set.append(str(qs_set_temp[c]))
        # ========寫入結果=========
    return qs_set
# ========從資料庫撈取符合對象=========可同時輸入多筆代號   結果會疊加  ex: find_q_set(1,4) 結果為 [異性男] 跟 [異性女] 集合

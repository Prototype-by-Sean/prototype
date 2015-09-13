# -*- coding: utf-8 -*-
from django.shortcuts import render
from datetime import date
from django.views.generic import ListView
from models import Member
from form import SearchForm
import filters_view
# Create your views here.


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


class HomePageView(ListView):
    model = Member
    queryset = Member.objects.all()
    context_object_name = 'members'
    template_name = 'match/home.html'

# =======ET=======


def search_view(request):
    if request.method == 'POST':
        form_in = request.POST
        # 字典型態{'a':[1,2],'b':[5,6],'c':[]}
        # ======定義使用者本身性別======
        try:
            my_biological_sex = Member.objects.filter(user=str(request.user))
        except:
            my_biological_sex = None
        # ======定義使用者本身性別======
        # =========分析找男女==========
        # 輸出 test_biological_sex        1:男女都選或都不選  2:女  3:男
        test_girl = 0
        test_boy = 0
        try:
            if len(form_in['find_girl']) > 0:
                test_girl = 1
        except:
            pass
        try:
            if len(form_in['find_boy']) > 0:
                test_boy = 1
        except:
            pass

        if test_girl == 1:
            if test_boy == 1:
                test_biological_sex = 1
            else:
                test_biological_sex = 2
        else:
            if test_boy == 1:
                test_biological_sex = 3
            else:
                test_biological_sex = 1
        del test_girl, test_boy
        # =========分析找男女==========
        # ======生成搜索用queryset======
        # 已轉換為清單內含字典格式(純PY)    ex : [{'id': 1, 'level_id': 2, 'job_id': 2, 'n.....
        q_set = None
        if my_biological_sex == '男':
            if test_biological_sex == 1:
                # 男女都撈(只撈性向
                q_set = filters_view.find_q_set(Member, 2, 3, 4, 6)
            if test_biological_sex == 2:
                # 撈女生
                q_set = filters_view.find_q_set(Member, 4, 6)
            if test_biological_sex == 3:
                # 撈男生
                q_set = filters_view.find_q_set(Member, 2, 3)
        elif my_biological_sex == '女':
            if test_biological_sex == 1:
                # 男女都撈(只撈性向
                q_set = filters_view.find_q_set(Member, 1, 3, 5, 6)
            if test_biological_sex == 2:
                # 撈女生
                q_set = filters_view.find_q_set(Member, 5, 6)
            if test_biological_sex == 3:
                # 撈男生
                q_set = filters_view.find_q_set(Member, 1, 3)
        else:
            if test_biological_sex == 1:
                # 男女都撈(只撈性向
                q_set = filters_view.find_q_set(Member, 1, 4, 2, 5, 3, 6)
            if test_biological_sex == 2:
                # 撈女生
                q_set = filters_view.find_q_set(Member, 4, 6)
            if test_biological_sex == 3:
                # 撈男生
                q_set = filters_view.find_q_set(Member, 1, 3)
        # ======生成搜索用queryset======
        # ====生成年齡範圍丟入filter=====
        # 生成 age_range = [10,11,12,13,14,15] 若無設定則生成 0 到 100
        if len(form_in['age_min']) != 0 or len(form_in['age_max']) != 0:  # 如果有輸入條件才開始進入過濾器
            if len(form_in['age_min']) == 0:
                age_min = 0  # 如果年齡最小值未輸入  則設為0
            else:
                age_min = int(form_in['age_min'])  # 如果年齡最小值有輸入  讀進來

            if len(form_in['age_max']) == 0:
                age_max = 300  # 如果年齡最大值未輸入  則設為300
            else:
                age_max = int(form_in['age_max'])  # 如果年齡最小值有輸入  讀進來
            q_set = filters_view.filter_age(Member, q_set, age_min, age_max)  # 過濾器參數 ( 資料庫 , 字典 , 最小值 , 最大值 )
        # ====生成年齡範圍丟入filter=====
        # ====生成身高範圍丟入filter=====
        if len(form_in['height_min']) != 0 or len(form_in['height_max']) != 0:
            if len(form_in['height_min']) == 0:
                height_min = 0
            else:
                height_min = int(form_in['height_min'])
            if len(form_in['height_max']) == 0:
                height_max = 300
            else:
                height_max = int(form_in['height_max'])
            q_set = filters_view.filter_height(Member, q_set, height_min, height_max)
        # ====生成身高範圍丟入filter=====
        # ====生成體重範圍丟入filter=====
        if len(form_in['weight_min']) != 0 or len(form_in['weight_max']) != 0:
            if len(form_in['weight_min']) == 0:
                weight_min = 0
            else:
                weight_min = int(form_in['weight_min'])
            if len(form_in['weight_max']) == 0:
                weight_max = 300
            else:
                weight_max = int(form_in['weight_max'])
            q_set = filters_view.filter_weight(Member,q_set,weight_min,weight_max)
        # ====生成體重範圍丟入filter=====
        # ==========過濾血型==========
        blood_type_list = request.POST.getlist('blood_type')  # 搜尋者要求的血型  為一清單型態  紀錄方式為 blood_type_id
        if len(blood_type_list) != 0:  # 如果清單內有東西(有搜尋條件)  才開始過濾
            q_set = filters_view.filter_blood_type(Member, q_set, blood_type_list)
        # ==========過濾血型==========
        # ==========過濾地點==========
        location_list = request.POST.getlist('location')
        if len(location_list) != 0:
            q_set = filters_view.filter_location(Member, q_set, location_list)
        # ==========過濾地點==========
        # ==========過濾信仰==========
        religion_list = request.POST.getlist('religion')
        if len(religion_list) != 0:
            q_set = filters_view.filter_religion(Member, q_set, religion_list)
        # ==========過濾信仰==========
        # ==========過濾關係==========
        relationship_list = request.POST.getlist('relationship')
        if len(relationship_list) != 0:
            q_set = filters_view.filter_relationship(Member, q_set, relationship_list)
        # ==========過濾關係==========
        # ========過濾感情狀態========
        relationship_status_list = request.POST.getlist('relationship_status')
        if len(relationship_status_list) != 0:
            q_set = filters_view.filter_relationship_status(Member, q_set, relationship_status_list)
        # ========過濾感情狀態========
        # ========過濾照片有無========
            # 待決議
        # ========過濾照片有無========
        # ========輸出優先名單========
        q_set_list = []
        for c1 in q_set:
            q_set_list.append([c1,int(q_set[c1])])
        q_set_list = sorted(q_set_list, key=lambda x: x[1], reverse=True)
        # ========輸出優先名單========
        end = q_set_list
        end1 = Member.objects.get(id=9).blood_type_id
        return render(request,'match/end.html',{'end': end,'end1':end1})
    else:
        form = SearchForm()
        ver1 = 'ver_view = %s' % (9131207,)
        return render(request,'match/test.html',{'test': form,'ver1':ver1})
# =======ET=======
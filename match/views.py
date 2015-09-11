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
                        if len(form_in['find_boy'])>0:
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
                # =========生成年齡範圍==========
                # 生成 age_range = [10,11,12,13,14,15] 若無設定則生成 0 到 100
                if len(form_in['age_max']) > 0 and len(form_in['age_min']) > 0:
                        age_range = list(range(int(form_in['age_min']),int(form_in['age_max'])+1))
                elif len(form_in['age_max']) > 0:
                        age_range = list(range(0,int(form_in['age_max'])+1))
                elif len(form_in['age_min']) > 0:
                        age_range = list(range(form_in['age_min'], 100))
                else:
                        age_range = list(range(0,100))
                # =========生成年齡範圍==========

                # dict_in = Member.objects.filter(age__in = form_in['age'])
                end = str(q_set)
                end1 = str(filters_view.filter_age(q_set,15,18))
                return render(request,'match/end.html',{'end': end,'end1':end1})
        else:
                form = SearchForm()
                return render(request,'match/test.html',{'test': form})
# =======ET=======
# -*- coding: utf-8 -*-
from django.shortcuts import render
from datetime import date
from django.views.generic import ListView
from models import Member
from form import SearchForm
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
        if request.method =='POST':
                form_in = request.POST          # 字典型態{'a':[1,2],'b':[5,6],'c':[]}
                use_name = str(request.user)    # 傳入name
                # =========生成年齡範圍==========
                #生成 age_range:[10,11,12,13,14,15] 若無設定則生成 0 到 100
                if len(form_in['age_max']) > 0 and len(form_in['age_min']) > 0:
                        form_in['age_range'] = list(range(int(form_in['age_min']),int(form_in['age_max'])+1))
                elif len(form_in['age_max']) > 0:
                        form_in['age_range'] = list(range(0,int(form_in['age_max'])+1))
                elif len(form_in['age_min']) > 0:
                        form_in['age_range'] = list(range(form_in['age_min'],100))
                else:
                        form_in['age_range'] = list(range(0,100))
                # =========生成年齡範圍==========


                # =========分析找男女==========
                # 1:男女  2:女  3:男  4:都不選
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
                                test_biological_sex = 4
                # =========分析找男女==========



                # dict_in = Member.objects.filter(age__in = form_in['age'])
                end = form_in
                return render(request,'match/end.html',{'end':end})
        else:
                form = SearchForm()
                return render(request,'match/test.html',{'test':form})
# =======ET=======
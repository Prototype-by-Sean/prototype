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
                # use_info = str(request.user)    # 傳入name
                test_girl = 0
                test_boy = 0
                # =========處理傳入需求==========
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
                                ttt = 1
                        else:
                                ttt = 2
                else:
                        if test_boy == 1:
                                ttt = 3
                        else:
                                ttt = 4




                # dict_in = Member.objects.filter(age__in = form_in['age'])
                end = ttt
                return render(request,'match/end.html',{'end':end})
        else:
                form = SearchForm()
                return render(request,'match/test.html',{'test':form})
# =======ET=======
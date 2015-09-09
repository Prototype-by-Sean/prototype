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
                form_in = {'age':[26,27]}
                use_info = str(request.user)    # 傳入name
                # =========處理傳入需求==========
                try:
                        pass
                        form_in['find_girl']
                        try:
                             pass
                             form_in['find_boy']
                        except:
                                pass
                                dict_in = Member.objects.filter(age__in = form_in['age'])
                except:
                        pass
                # =========處理傳入需求==========

                #for c in form_in:
                        #if c !='submit' and c !='csrfmiddlewaretoken' and len(form_in[c]) != 0:
                                #分單次搜索根多次搜索 分開查詢

                dict_in = Member.objects.filter(age__in = form_in['age'])
                                #pass
                end = dict_in
                return render(request,'match/end.html',{'end':end})
        else:
                form = SearchForm()
                return render(request,'match/test.html',{'test':form})
# =======ET=======
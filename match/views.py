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
                form_in = request.POST
                #for c in form_in:
                        #if c !='submit' and c !='csrfmiddlewaretoken' and len(form_in[c]) != 0:
                                #分單次搜索根多次搜索 分開查詢
                                #pass
                end = str(form_in)
                return render(request,'match/end.html',{'end':end})
        else:
                form = SearchForm()
                return render(request,'match/test.html',{'test':form})
# =======ET=======
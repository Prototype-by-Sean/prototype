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

#=======ET=======
def SearchView(request):
        if request.method =='POST':
                form = SearchForm()
        else:
                form = SearchForm()
        return render(request,'match/test.html',{'test':form})
#=======ET=======
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView,FormView
from django.urls import reverse_lazy
from change.models import Change, Coin
from change.forms import ChangeForm

# Create your views here.
class MakeChangeView(FormView):
    model = Change
    form_class = ChangeForm
    template_name = 'pages/make_change.html'
    success_url = 'view_change'

    def form_valid(self,form):
        form.save()
        total_coins,list_of_coins = form.instance.make_change_1()
        form.instance.total_count = total_coins
        form.save()
        form.instance.save_coins(list_of_coins)
        return super().form_valid(form)

class ViewChange(ListView):
    model = Change
    template_name = 'pages/recent_change.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ViewChange,self).get_context_data(*args,**kwargs)
        change = Change.objects.last()
        print('last',change)
        coins = Coin.objects.filter(change=change)
        context['recent_change'] = change
        context['coins'] = coins
        return context
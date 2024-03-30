from django.shortcuts import render,get_object_or_404
from django.views.generic.list import ListView
from .models import Goods
from django.views.generic.detail import DetailView
# Create your views here.

class Products(ListView):
    model=Goods
    queryset=Goods.objects.all()
    template_name='index.html'
    context_object_name='pack'



class Detail(DetailView):
    model=Goods
    template_name='detail.html'
    context_object_name='details'

    def get_object(self, queryset=None):
        # Retrieve the parameter value from the URL
        pk = self.kwargs.get('pk')
        # Use the parameter value to filter the queryset
        queryset = Goods.objects.filter(pk=pk)
        # Call the superclass method to get the object
        return super().get_object(queryset)
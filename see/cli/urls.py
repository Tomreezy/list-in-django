from . import views
from django.urls import path

app_name='cli'


urlpatterns=[
    path('',views.Products.as_view(), name='index'),
    path('<int:pk>/',views.Detail.as_view(), name='Detail'),
]
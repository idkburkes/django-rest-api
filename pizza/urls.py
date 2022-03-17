from django.urls import path
from .views import PizzaList, PizzaDetail

urlpatterns = [
    path('', PizzaList.as_view(), name='pizza_list'),
    path('<int:pk>/', PizzaDetail.as_view(), name='pizza_detail')
]
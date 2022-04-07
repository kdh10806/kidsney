from django.urls import path

from .views import OrderView, CashView

urlpatterns = [
    path('', OrderView.as_view()),
    path('/cash', CashView.as_view())
] 
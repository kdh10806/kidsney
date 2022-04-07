from django.urls import path

from .views import MainProductView, ProductDetailView, SearchView

urlpatterns = [
    path('', MainProductView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()),
    path('/search', SearchView.as_view())
]
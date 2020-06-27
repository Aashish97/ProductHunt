from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.createproduct, name='create'),
    path('<int:product_id>/', views.productdetail, name='detail'),
    path('<int:product_id>/upvote/', views.upvote, name='upvote'),
]
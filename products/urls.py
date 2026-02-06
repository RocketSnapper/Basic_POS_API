from django.urls import path
from . import views

urlpatterns = [     
    path('add/', views.add),
    path('<int:pk>/', views.remove),
    path('payment/', views.payment)
]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('handy/dash', views.handyDashView.as_view(), name="dash"),
    path('handy/dash/view/<int:pk>/', views.serviceView.as_view(), name="view"),
    path('handy/dash/view/<int:pk>/apply', views.requestServiceView.as_view(), name="apply"),
]
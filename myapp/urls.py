from django.urls import path
from myapp import views
urlpatterns = [
    path(r'', views.HomePageView.as_view()),
]
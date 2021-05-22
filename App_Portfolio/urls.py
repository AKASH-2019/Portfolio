from django.urls import path
from .import views

app_name = 'App_Portfolio'


urlpatterns = [
	path('', views.home, name="home"),
	path('project-list', views.list, name="list"),
	path('project_detail/<str:pk>/', views.project_detail, name="project-detail"),
	path('contact', views.contact, name="contact"),

]
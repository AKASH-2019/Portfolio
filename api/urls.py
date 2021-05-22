from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
    path('project-list/', views.projectList, name="project-list"),
	path('project-detail/<int:pk>/', views.projectDetail, name="project-detail"),
	path('project-create/', views.projectCreate, name="project-create"),
	
	path('project-update/<str:pk>/', views.projectUpdate, name="project-update"),
	path('project-delete/<str:pk>/', views.projectDelete, name="project-delete"),

]
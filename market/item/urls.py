from django.urls import path

from .import views

app_name = 'item'

# pk has to be the same as the pk in views
urlpatterns = [
    path('<int:pk>/', views.detail, name='detail')
]

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.custom_login, name='login'),  # Use custom login view
    path('logout/', views.custom_logout, name='logout'),
    path('', views.home, name='home'),
    path('chat/<int:user_id>/', views.chat, name='chat'),
    # path('', include('chatapp.urls'))

]
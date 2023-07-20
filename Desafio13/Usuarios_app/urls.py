from django.urls import path 
from usuarios_app import views
from django.contrib.auth.views import LoginView, LogoutView
app_name = "usuarios_app"

urlpatterns = [
	path('login/', LoginView.as_view(template_name = 'login.html', name = 'login')),
    path('logout/', LogoutView.as_view(next_page= 'login/',name = 'logout'))   
] 

"""nemisis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from online_portal import views
# from online_portal.views import UserUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home , name = 'home'),

    # Auth
    path('signup/',views.usersignup,name = 'signupuser'),
    path('logout/',views.logoutuser,name = 'logoutuser'),
    path('login/',views.loginuser,name = 'loginuser'),

    # Editing and displaying User Details
    path('details/',views.userdetails,name = 'userdetails'),
    # path('edituser/<int:user_id>',views.update_profile,name = 'update_profile'),
    path('update/<int:user_id>/',views.update_profile,name = 'update_profile'),
    path('userdelete/<int:user_id>' , views.delete_user , name = 'userdelete'),
    path('edituserdetails/<int:user_id>' , views.edituserdetails , name = 'edituserdetails')
]

"""login_webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("login_system.urls")),
    path("contact/",include("home.urls")),
    #path("creator_contact/",include("home.urls")),
    path("photo/", include("home.urls")),
    path("admin_login/", include("login_system.urls")),
    path("register/", include("login_system.urls")),
    #path("after_login/", include("login_system.urls")),
    #path("show_data/", include("login_system.urls")),
    path("profile/", include("login_system.urls")),
    path("stu_profile/", include("login_system.urls")),
    path("login_out/", include("login_system.urls")),
    path("apan/", include("login_system.urls")),
    path("pan/<int:id>/", include("login_system.urls")),
    path("show-and-upload-questions/<int:admin_id>/", include("login_system.urls")),
    path("answer/<int:id>/<int:que>/<int:admin_id>/", include("login_system.urls")),
    path("delete_question/<int:admin_id>/<int:question>/", include("login_system.urls")),
    path("question/<int:admin_id>/", include("login_system.urls")),
    path("reder/", include("login_system.urls")),
   # path("time_table/", include("login_system.urls")),
    path("adhar/<int:id>/", include("login_system.urls")),
    path("admin_back/<int:admin_id>/", include("login_system.urls")),
    path("aprofile_photo/", include("login_system.urls")),
    path("add_marks/<int:id>/<int:que_no>/<int:admin_id>/", include("login_system.urls")),
    path("profile_photo/", include("login_system.urls")),
    path("userlogin/", include("login_system.urls")),
    path("view_pan/<int:id>/", include("login_system.urls")),
    path("back_front/<int:id>/", include("login_system.urls")),
    path("delete/<int:id>/", include("login_system.urls")),
    path("update/<int:id>/<int:admin_id>/", include("login_system.urls")),
    path("edit_user/<int:id>/", include("login_system.urls")),
    path("back_front/", include("login_system.urls")),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# we can also change the admin pannel layout,title search on google.
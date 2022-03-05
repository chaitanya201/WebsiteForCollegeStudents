from django.urls import path
from login_system import views


urlpatterns=[
path('', views.index,name="home"),
    path("admin_login/",views.admin_login_page, name="login_page" ),
    path("register/",views.register,name="register"),

    #path("show_data/",views.show_data,name="show_data"),
    ##path("profile/",views.profile,name="profile"),
    path("stu_profile/",views.profile,name="student_profile"),
    path("pan/<int:id>/",views.upload_pan,name="pancard"),
    path("answer/<int:id>/<int:que>/<int:admin_id>/",views.upload_answers,name="ans"),
    path("question/<int:admin_id>/",views.add_que,name="que"),
    path("delete_question/<int:admin_id>/<int:question>/",views.delete_question,name="delete_que"),
    #path("apan/",views.admin_upload_pan,name="apancard"),
    #path("time_table/",views.admin_upload_timetable,name="time_table"),
    path("adhar/<int:id>/",views.upload_adhar, name="adharcard"),
    path("contact/",views.contact,name='contact'),
    path("view_pan/<int:id>/",views.view_pan, name="view_pan"),
    path("view_adhar/<int:id>/",views.view_adhar, name="view_adhar"),
    path("back_front/<int:id>/",views.front, name="front"),
    path("admin_back/<int:admin_id>/",views.admin_back, name="admin_back"),
    path("add_marks/<int:id>/<int:que_no>/<int:admin_id>/", views.add_marks, name='add_marks'),
    path("delete/<int:id>/",views.delete_user, name="delete"),
    path("show-and-upload-questions/<int:admin_id>/",views.show_and_upload_questions, name="show_and_upload_questions"),
    path("update/<int:id>/<int:admin_id>/",views.update_user, name="update"),
    path("edit_user/<int:id>/",views.edit_profile, name="edit_details"),
    path("login_out/",views.log_out, name="log_out"),
    path("add_user/",views.add_user, name="add_user"),
    #path("reder/",views.rendering,name="render_file"),
    path("profile_photo/",views.upload_profile, name="ProfilePhoto"),
#    path("aprofile_photo/",views.admin_upload_profile,name="aProfilePhoto"),
    path("userlogin",views.user_login,name="UserLogin"),


]
# if the path is login in the main urls file and it includes the another file say login_system's urls file.
# then we can open any url in the login_system's urls file using the login url.
# e.g :- if the path is login/after_login then control will go like below
# first it will go to main urls file (login_webapp's urls) then it will go to urls file of login_system after that we can go
# to the any url in login_system's urls file. we can open any url in login_system's urls file through "login" path of main urls file.
#here it will run after_login function in view file of login_system app.
# anothe e.g:- if path is register/ by writing only this contol goes to the urls file of the login_system' app
# if we write login after register i.e if path is register/login then view.login will hit.
# conclusion:-
    # if we want to render the after_login file then we have to give the path like
    # after_login/after_login  or
    # register/after_login  or
    # login/after_login
    # before "/" we can give any path name which includes the login_system's urls file and after "/" we give the required path  name
    # which we want to run.
    #  in our case after_login/after_login this path make more sense. but we can use any of the mentioned path.
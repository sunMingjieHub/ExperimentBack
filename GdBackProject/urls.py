"""GdBackProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from GdPro import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'login',views.login),  # 登录接口

    path(r'clname', views.get_class_name),  # 获取班级名称
    path(r'teacher/<teacher_id>', views.get_my_experiment), #获取教师自己的实验安排
    path(r'sname', views.get_seat_name), # 获取座区信息
    path(r'coname', views.get_all_course), # 获取所有课程信息
    path(r'teacher/delete/ban',views.delete_experiment_by_ban), #删除某个班某个课程
    path(r'all_teacher', views.get_teachers),   #获取所有教师信息

    path(r'add_teacher', views.add_teacher),
    path(r'add_class', views.add_class),
    path(r'add_seat', views.add_seat),
    path(r'add_course', views.add_course),

    path(r'reset', views.reset_password),

    path(r'deleteteacher',views.delete_teacher),
    path(r'deleteseat', views.delete_seat),
    path(r'deleteclass', views.delete_class),
    path(r'deletecourse', views.delete_course),

    path(r'all_experiment_count', views.get_experiment_count), #返回课时数
    path(r'weekExp/<week_number>', views.get_week_experiment),  # 返回课时数
    path(r'add_experiment', views.add_exp),  # 返回课时数会实验
    path(r'clexperiment/<class_id>', views.class_experiment), #根据班级fan
    path(r'experiment_detail', views.experiment_detail),
    path(r'class_experiment_detail',views.class_experiment_detail)
]

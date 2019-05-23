from django.http import HttpResponse
import json
from .constant import *
from .methods_util import *
import logging


# Create your views here.

# 登录
def login(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        re = authoricate(uname, pwd)
        if re == -999:
            result = {'status': ERROR_NAME_PWD}
        else:
            result = {'status': SUCCESS, 'tid': re}
    else:
        result = {'status': ERROR_REQUIR}
        logging.warning(result)
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")


# 获取老师自己的实验简略信息
def get_my_experiment(request, teacher_id):
    if request.method == "GET":
        result = {'exp': get_experiment(teacher_id), 'code': SUCCESS}
    else:
        result = {'code': ERROR}
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")


# 根据班级获取实验信息
def class_experiment(request ,class_id):
    if request.method == 'GET':
        result = {'clexp':get_class_experiment(class_id), 'code': SUCCESS}
    else:
        result = {'code': ERROR}
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")


# 获取所有课程信息
def get_all_course(request):
    if request.method == "GET":
        result = {'courses': get_all_name(Course), 'code': SUCCESS}
    else:
        result = {'code': ERROR}
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")


# 获取所有班级信息
def get_class_name(request):
    if request.method == "GET":
        result = {'al_class': get_all_name(Expclass), 'code': SUCCESS}
    else:
        result = {'code': ERROR}
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")


# 获取所有教师信息
def get_teachers(request):
    if request.method == "GET":
        result = {'teachers': get_all_teacher_info(), 'code': SUCCESS}
    else:
        result = {'code': ERROR}
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")


# 获取所有座区信息
def get_seat_name(request):
    if request.method == "GET":
        result = {'seats': get_all_name(Address), 'code': SUCCESS}
    else:
        result = {'code': ERROR}
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")


# 删除某班某实验
def delete_experiment_by_ban(request):
    print(request.POST)
    if request.method == 'POST':
        res = delete_experiment_by_teacher(request.POST.get('t_id'), request.POST.get('cl_id'), request.POST.get('co_id'))
        print(res)
        if res:
            result={'code': SUCCESS}
        else:
            result={'code': ERROR}
    else:
        result = {'code': ERROR}
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")


def add_teacher(request):
    if request.method == 'POST':
        t_name = request.POST.get('t_name')
        account = request.POST.get('t_account')
        res = add_teacher_by_account(t_name, account)
        if res:
            result = {'code': 200}
        else:
            result = {'code': 500}

    return HttpResponse(json.dumps(result,ensure_ascii=False),content_type='application/json,charset=utf-8')


def add_class(request):
    if request.method == 'POST':
        cl_name = request.POST.get('name')
        res = add_by_name(Expclass,cl_name);
        if res:
            result = {'code': 200}
        else:
            result = {'code': 500}

    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json,charset=utf-8')


def add_seat(request):
    if request.method == 'POST':
        seat_name = request.POST.get('name')
        res = add_by_name(Address, seat_name);
        if res:
            result = {'code': 200}
        else:
            result = {'code': 500}

    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json,charset=utf-8')


def add_course(request):
    if request.method == 'POST':
        course_name = request.POST.get('name')
        res = add_by_name(Course, course_name);
        if res:
            result = {'code': 200}
        else:
            result = {'code': 500}

    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json,charset=utf-8')


def reset_password(request):
    if request.method == 'POST':
        account = request.POST.get('t_account')
        res = reset_password_by_account(account)
        if res:
            result = {'code': 200}
        else:
            result = {'code': 500}

    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json,charset=utf-8')


def delete_teacher(request):
    if request.method == 'POST':
        t_id = request.POST.get("t_id")
        delete_by_id(Teacher,t_id)
        delete_experiment_by_tid(t_id)
        result = {'code': 200}
        return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json,charset=utf-8')


def delete_seat(request):
    if request.method == 'POST':
        s_id = request.POST.get("id")
        delete_by_id(Address, s_id)
        delete_experiment_by_sid(s_id)
        result = {'code': 200}
        return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json,charset=utf-8')


def delete_class(request):
    if request.method == 'POST':
        cl_id = request.POST.get("id")
        delete_by_id(Expclass, cl_id)
        delete_experiment_by_clid(cl_id)
        result = {'code': 200}
        return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json,charset=utf-8')


def delete_course(request):
    if request.method == 'POST':
        co_id = request.POST.get("id")
        delete_by_id(Course, co_id)
        delete_experiment_by_coid(co_id)
        result = {'code': 200}
        return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json,charset=utf-8')


def get_experiment_count(request):
    if request.method == 'GET':
        exp = get_count()
        result = {'code': 200, 'experiment': exp}
        return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json,charset=utf-8')


def get_week_experiment(request, week_number):
    if request.method == 'GET':
        exp = get_experiment_by_week(week_number)
        result = {'code': 200, 'experiment': exp}
        return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json,charset=utf-8')


def add_exp(request):
    if request.method == 'POST':
        data =  json.loads(request.body.decode())

        t_id = data.get('teacher_id')
        cl_id = data.get('class_id')
        co_id = data.get('course_id')
        seats = data.get('seats')
        weeks = data.get('weeks')
        terms = data.get('days')
        times = data.get('times')

        res = add_experiment(t_id,cl_id,co_id,seats,weeks,terms,times)
        if res:
            result = {'code': 200}
        else:
            result = {'code': 502}
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json,charset=utf-8')


def experiment_detail(request):
    if request.method == 'POST':
        t_id = request.POST.get('teacher_id')
        cl_id = request.POST.get('class_id')
        co_id = request.POST.get('course_id')
        result = {'experiment': get_experiment_detail(t_id, cl_id, co_id), 'code': SUCCESS}
    else:
        result = {'code': ERROR}
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json,charset=utf-8')


def class_experiment_detail(request):
    print(request.POST)
    if request.method == 'POST':
        cl_id = request.POST.get('class_id')
        co_id = request.POST.get('course_id')
        result = {'experiment': get_class_experiment_detail(cl_id, co_id), 'code': SUCCESS}
    else:
        result = {'code': ERROR}
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json,charset=utf-8')



from .models import *


# 认证教师登录信息
def authoricate(account, pwd):
    try:
        set = Teacher.objects.get(account=account)
        if set is not None and set.password == pwd:
            return set.id
        else:
            return -999
    except Teacher.DoesNotExist:
        return -999


# 返回简略的实验信息，包括id，教师id,姓名，班级id，课程id
def get_experiment(teacher_id):
    set = Experiment.objects.filter(teacherid=teacher_id)
    print(len(set))
    result = []
    for var in set:
        teacher_name = Teacher.objects.get(id=teacher_id).name
        class_name = Expclass.objects.get(id=var.classid).name
        course_name = Course.objects.get(id=var.courseid).name
        item = {'t_id': teacher_id, 'teacher_name': teacher_name, 'cl_id': var.classid, 'class_name': class_name,
                'co_id': var.courseid, 'course_name': course_name}
        if item not in result:
            result.append(item)
    print(result)
    return result


def get_count():
    set = Experiment.objects.all()
    result =[]
    for var in set:
        teacher = Teacher.objects.get(id = var.teacherid).name
        class_name = Expclass.objects.get(id = var.classid).name
        course_name = Course.objects.get(id = var.courseid).name
        item = {'teacher': teacher, 'teacherid':var.teacherid, 'class_name': class_name, 'classid':var.classid, 'courseid':var.courseid, 'course_name': course_name}
        if item not in result:
            result.append(item)
    print(result)
    for var in result:
        n = Experiment.objects.filter(teacherid=var.get('teacherid'), classid=var.get('classid'), courseid=var.get('courseid')).count()
        var['count'] = 2*n
    print(result)
    return result

# 通过指定信息删除实验
def delete_experiment_by_id(teacher_id, class_id, course_id):
    print(teacher_id, class_id, course_id)
    try:
        set = Experiment.objects.filter(teacherid=teacher_id, courseid=course_id, classid=class_id)
        for s in set:
            s.delete()
        return True
    except:
        return False


def delete_experiment_by_tid(tid):
    try:
        set = Experiment.objects.filter(teacherid=tid)
        for s in set:
            s.delete()
        return True
    except:
        return False


def delete_experiment_by_teacher(t_id, cl_id, co_id):
    print(t_id, cl_id, co_id)
    try:
        mset = Experiment.objects.filter(teacherid=t_id, classid=cl_id, courseid=co_id)
        print(len(mset))
        for s in mset:

            s.delete()
        return True
    except:
        return False



def delete_experiment_by_sid(sid):
    try:
        set = Experiment.objects.filter(addressid =sid)
        for s in set:
            s.delete()
        return True
    except:
        return False


def delete_experiment_by_clid(tid):
    try:
        set = Experiment.objects.filter(classid=tid)
        for s in set:
            s.delete()
        return True
    except:
        return False


def delete_experiment_by_coid(tid):
    try:
        set = Experiment.objects.filter(courseid=tid)
        for s in set:
            s.delete()
        return True
    except:
        return False


def delete_by_id(model, _id):
    try:
        obj = model.objects.get(id=_id)
        obj.delete()
        return True
    except:
        return False


# 返回所有班级名称
def get_all_name(model):
    cllist = model.objects.all()
    result = []
    for var in cllist:
        item = {'id': var.id, 'name': var.name}
        result.append(item)
    print(model)
    print(result)
    return result


def get_all_teacher_info():
    teachers = Teacher.objects.all()
    result = []
    for var in teachers:
        item = {'t_id': var.id, 't_name': var.name, 't_account': var.account, 't_password': var.password}
        result.append(item)
    print(result)
    return result


# 增加教师
def add_teacher_by_account(tname, taccount):
    res = Teacher.objects.filter(account=taccount)
    print(res, tname, taccount)
    if len(res) != 0:
        return False
    else:
        new_teacher = Teacher(name=tname, account=taccount, password='123456')
        new_teacher.save()
        return True



def add_by_name(model,model_name):
    res = model.objects.filter(name=model_name)
    if len(res) != 0:
        return False
    else:
        new_class = model(name=model_name)
        new_class.save()
        return True


# 重置密码为123456
def reset_password_by_account(t_account):
    ter = Teacher.objects.get(account=t_account)
    ter.password = '123456'
    ter.save()
    return True


# 获取当前周次的实验
def get_experiment_by_week(week_number):
    all_experiment = Experiment.objects.filter(weeknumber=week_number)
    res = []
    lists = [[[] for _ in range(4)] for _ in range(5)]
    for var in all_experiment:
        teacher_name = Teacher.objects.get(id=var.teacherid).name
        class_name = Expclass.objects.get(id=var.classid).name
        course_name = Course.objects.get(id=var.courseid).name
        seat_name = Address.objects.get(id=var.addressid).name

        # 周几
        term = var.term
        # 第几大节
        time = var.time
        item = {'teacher_name': teacher_name, 'teacher_id': var.teacherid, 'class_name': class_name,
                'course_id': var.courseid, 'course_name': course_name, 'day': term, 'seat_name': seat_name,
                'time': time}
        if item not in res:
            res.append(item)
    temp = {}
    temp1 = {}
    for item in res:
        key = item.get('teacher_name')+","+item.get('course_name')+" "+str(item.get('day'))+" "+str(item.get('time'))
        temp[key] = ""
    for item in res:
        key = item.get('teacher_name')+","+item.get('course_name')+" "+str(item.get('day'))+" "+str(item.get('time'))
        temp[key] = temp[key]+item.get('class_name')
    for item in res:
        key = item.get('teacher_name') + "," + item.get('course_name') + " " + str(item.get('day')) + " " + str(
            item.get('time'))
        temp[key] = temp[key] + ' '
    for item in res:
        key = item.get('teacher_name') + "," + item.get('course_name') + " " + str(item.get('day')) + " " + str(
            item.get('time'))
        temp[key] = temp[key]+item.get('seat_name')

    for key in temp:
        tem = key.split()
        lists[int(tem[1])-1][(int(tem[2])-1)].append(tem[0]+","+temp[key])


    result = [[] for _ in range(5)]

    for i in range(5):
        for j in range(4):
            item = lists[i][j]
            if len(item) == 1:
                ex = item[0]
                for k in range(3 - len(item)):
                    lists[i][j].append(ex)
            else:
                for k in range(3-len(item)):
                    lists[i][j].append('')
            item = lists[i][j]
            for var in item:
                result[i].append(var)

    print(result)
    return result


# 添加实验
def add_experiment(t_id, cl_id, co_id, seats, weeks, terms, times):
    print(t_id, cl_id, co_id, seats, weeks, terms, times)
    CanSave = True
    for week in weeks:
        for te in terms:
            for ti in times:
                # 班级是否冲突
                mset2 = Experiment.objects.filter(classid=cl_id, weeknumber=week, term=te, time=ti)
                if len(mset2) != 0:
                    print("---")
                    CanSave = False
                    break
                #   座区是否冲突
                for seat in seats:
                    mset3 = Experiment.objects.filter(addressid=seat, weeknumber=week, term=te, time=ti)
                    if len(mset3) != 0:
                        print("---")
                        CanSave = False
                        break
    if CanSave:
        for week in weeks:
            for te in terms:
                for ti in times:
                    for seat in seats:
                        experiment_new = Experiment(teacherid=t_id,
                                                    classid=cl_id,courseid=co_id,weeknumber=week,
                                                    term=te,time=ti,addressid=seat)
                        experiment_new.save()
                        print("添加成功")
        return True
    else:
        return False


def get_class_experiment(class_id):
    mset = Experiment.objects.filter(classid=class_id)
    res = []
    for var in mset:
        teacher_name = Teacher.objects.get(id=var.teacherid).name
        class_name = Expclass.objects.get(id=class_id).name
        course_name = Course.objects.get(id=var.courseid).name
        item = {'class_id': class_id,'class_name': class_name,'course_id':var.courseid, 'course_name': course_name,'teacher_id':var.teacherid, 'teacher_name': teacher_name}
        if item not in res:
            res.append(item)
    return res


def get_experiment_detail(t_id, cl_id, co_id):
    mset = Experiment.objects.filter(teacherid=t_id, classid=cl_id, courseid=co_id)
    res =[]
    temp= {}
    for var in mset:
        item = {'week': var.weeknumber, 'day': var.term, 'time': var.time,'seat':Address.objects.get(id=var.addressid).name}
        if item not in res:
            res.append(item)

    for var in res:
        key = str(var.get('week')) + ',' + var.get('day') + ',' + str(var.get('time'))
        temp[key] = ""
    for var in res:
        key = str(var.get('week')) + ',' + var.get('day') + ',' + str(var.get('time'))
        temp[key] = temp[key]+ var.get('seat')
    tmp =[]
    for var in res:
        key = str(var.get('week')) + ',' + var.get('day') + ',' + str(var.get('time'))
        item = {'week': "第 "+str(var.get('week'))+" 周" ,'day': "星期"+var.get('day') ,'time':"第"+ str(var.get('time'))+"大节", 'seats': temp[key]}
        if item not  in tmp:
            tmp.append(item)
    return tmp


def get_class_experiment_detail(cl_id, co_id):
    print(cl_id, co_id)
    mset = Experiment.objects.filter(classid=cl_id, courseid=co_id)
    res = []
    temp = {}
    for var in mset:
        item = {'week': var.weeknumber, 'day': var.term, 'time': var.time, 'teacher': Teacher.objects.get(id=var.teacherid).name,'course':Course.objects.get(id=co_id).name,
                'seat': Address.objects.get(id=var.addressid).name}
        if item not in res:
            res.append(item)

    for var in res:
        key = str(var.get('week')) + ',' + var.get('day') + ',' + str(var.get('time'))
        temp[key] = ""
    for var in res:
        key = str(var.get('week')) + ',' + var.get('day') + ',' + str(var.get('time'))
        temp[key] = temp[key] + var.get('seat')
    tmp = []
    for var in res:
        key = str(var.get('week')) + ',' + var.get('day') + ',' + str(var.get('time'))
        item = {'week': "第 " + str(var.get('week')) + " 周", 'day': "星期" + var.get('day'),'teacher': var.get('teacher'),'course':var.get('course'),
                'time': "第" + str(var.get('time')) + "大节", 'seats': temp[key]}
        if item not in tmp:
            tmp.append(item)
    print(tmp)
    return tmp
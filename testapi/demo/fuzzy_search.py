

#搜索功能

@csrf_exempt#使用@csrf_exempt装饰器，免除csrf验证
def search_testCaseApi(request):
    if request.method == 'POST':
        name = request.POST.get('task_name')
        updateUser=request.POST.get('task_updateUser')
        if name=="" and updateUser=="":
            obj_all = tnw_test_case_api.objects.filter(del_flag=0)
        elif name!="" and updateUser=="":
            obj_all = tnw_test_case_api.objects.filter(del_flag=0,case_name__contains=name)
        elif name=="" and updateUser!="":
            obj_all = tnw_test_case_api.objects.filter(del_flag=0,update_user__contains=updateUser)
        else:
            obj_all = tnw_test_case_api.objects.filter(del_flag=0,case_name__contains=name,update_user__contains=updateUser)
        ApiCasesList = []
        for li in obj_all:
            need_interfacename = allFunction().get_interfaceName(li.id)
            api_list, api_sum = allFunction().testIDConnect_needid(li.id)
            if li.case_module is not None:
                ApiCasesList.append({
                    "testCaseApi_id": li.id,
                    "testCaseApi_name": li.case_name,
                    "testCaseApi_sum": api_sum,
                    "testCaseApi_version": li.case_version,
                    "testCaseApi_module": li.case_module,
                    "testCaseApi_need_interfacename": need_interfacename,
                    "testCaseApi_createTime": str(li.create_time),
                    "testCaseApi_updateTime": str(li.update_time),
                    "testCaseApi_updateUser": li.update_user,
                })
            else:
                ApiCasesList.append({
                    "testCaseApi_id": li.id,
                    "testCaseApi_name": li.case_name,
                    "testCaseApi_sum": 1,
                    "testCaseApi_version": li.case_version,
                    "testCaseApi_module": li.case_module,
                    "testCaseApi_need_interfacename": need_interfacename,
                    "testCaseApi_createTime": str(li.create_time),
                    "testCaseApi_updateTime": str(li.update_time),
                    "testCaseApi_updateUser": li.update_user,
                })
        # 将int类型使用dumps()方法转为str类型
        ApiCasesList_len = json.dumps(len(ApiCasesList))
        # 构造一个字典
        json_data_list = {'rows': ApiCasesList, 'total': ApiCasesList_len}
        # dumps()将字典转变为json形式,
        easyList = json.dumps(json_data_list)
        # 将json返回去，json的键值对中的键需要与前台的表格field=“X”中的X名称保持一致）
        return HttpResponse(easyList)
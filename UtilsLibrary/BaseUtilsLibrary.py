import uuid
import random
import time
import xlwt
import math
from itertools import combinations


class BaseUtilsLibrary(object):
    # 获取字符串形式UUID,32位无"-"连接
    @staticmethod
    def get_uuid():
        ids = uuid.uuid1()
        ids = str(ids)
        ids = ids.replace("-", "")
        return ids

    # 生成随机车牌号
    @staticmethod
    def get_car_id():
        data = "辽A"
        for index in range(0, 5):
            num = random.randint(0, 9)
            chars = chr(random.randint(65, 91))
            if (random.randint(0, 9)) % 2 == 0:
                data = data + str(num)
            else:
                data = data + str(chars)
        return data

    # 生成1开头定长数字,默认11位
    @staticmethod
    def make_num(end=11):
        mobile_num = "1"
        for i in range(1, end):
            num = random.randint(0, 9)
            print(num)
            mobile_num = mobile_num + str(num)
        return mobile_num

    # 生成时间戳
    @staticmethod
    def make_time():
        return str(time.time())

    # 获取北京时间当前秒数
    @staticmethod
    def make_now_second():
        return int(str(time.time())[0:10]) % 86400 + 8 * 60 * 60

    @staticmethod
    def add_number(x, y):
        return int(x) + int(y)

    # 生成时间戳
    @staticmethod
    def make_time_as_string():
        time_str = str(time.time())
        time_str = time_str.replace(".", "")
        return time_str

    # 状态码错误等级判定逻辑
    @staticmethod
    def auto_create_bug_level_tag(resp_code, status_code):
        bug_level = None
        resp_code = int(resp_code)
        status_code = int(status_code)
        if status_code == 200 and resp_code in (201, 204):
            bug_level = 'Major'
        if status_code == 200 and resp_code == 202:
            bug_level = 'Critical'
        if status_code in (201, 204) and resp_code == 200:
            bug_level = 'Major'
        if status_code == 201 and resp_code in (202, 204):
            bug_level = 'Critical'
        if status_code == 204 and resp_code == 201:
            bug_level = 'Major'
        if status_code == 204 and resp_code == 202:
            bug_level = 'Critical'
        if status_code in (200, 201, 202, 204) and resp_code in (400, 401, 403, 404, 405, 410, 422):
            bug_level = 'Critical'
        if status_code in (301, 302, 304) and resp_code in (301, 302, 304) and status_code != resp_code:
            bug_level = 'Major'
        if status_code == 400 and resp_code in (200, 201, 202, 204):
            bug_level = 'Major'
        if status_code == 400 and resp_code in (301, 302, 304):
            bug_level = 'Major'
        if status_code == 400 and resp_code in (401, 403, 404, 405, 410, 422):
            bug_level = 'Minor'
        if status_code in (401, 403) and resp_code in (200, 201, 202, 204):
            bug_level = 'Critical'
        if status_code in (401, 403) and resp_code in (400, 404, 405, 410, 422):
            bug_level = 'Minor'
        if status_code in (404, 410) and resp_code in (200, 201, 202, 204):
            bug_level = 'Major'
        if status_code in (404, 410) and resp_code in (400, 401, 405, 403, 422):
            bug_level = 'Major'
        if status_code == 405 and resp_code in (200, 201, 202, 204):
            bug_level = 'Major'
        if status_code == 405 and resp_code in (400, 401, 403, 404, 410, 422):
            bug_level = 'Minor'
        if status_code == 422 and resp_code in (200, 201, 202, 204):
            bug_level = 'Critical'
        if status_code == 422 and resp_code in (400, 401, 403, 404, 405, 410):
            bug_level = 'Major'
        if resp_code == 500:
            bug_level = 'Blocker'
        if resp_code == 502:
            bug_level = 'Minor'
        if resp_code == 504:
            bug_level = 'Minor'
        if status_code == 405 and resp_code in (301, 302, 304):
            bug_level = 'Major'
        if bug_level is not None:
            bug_level = 'BugLevel:' + bug_level
        return bug_level

    # 状态码动态提示逻辑
    @staticmethod
    def auto_create_status_tag(resp_code, status_code):
        status_tag = None
        if str(resp_code) != str(status_code):
            status_tag = 'ShouldBe:'+str(status_code)+'But:'+str(resp_code)
        return status_tag

    # 生成excel表 (行数, 第一行名称列表, 名称对应的值列表, 表名, 文件名) 列表最多256个元素
    @staticmethod
    def write_xls(rows, cols_name, cols_value, sheet_name, file_name):
        rows = int(rows)
        cols_name = cols_name.split(",")
        cols_value = cols_value.split(",")
        times = int(math.ceil(rows/65535))
        this_rows = 0
        work_book = xlwt.Workbook(encoding='utf-8')
        for _ in range(0, times):
            sheet = work_book.add_sheet(str(sheet_name)+str(_))
            if rows <= 65534:
                this_rows = rows + 1
            elif rows > 65534:
                this_rows = 65535
                rows -= 65534
            for i in range(0, this_rows):
                for j in range(0, len(cols_name)):
                    if i == 0:
                        sheet.write(i, j, str(cols_name[j]))
                    else:
                        sheet.write(i, j, str(cols_value[j]))
        work_book.save(str(file_name))

    # # 自动生成所有组合方式的参数列表
    # @staticmethod
    # def auto_params(essential_params, unessential_params, success=True):
    #     data = []
    #     results = []
    #     params = ''
    #     start_num = 0
    #     index = 0
    #     if success is False:
    #         start_num = 1
    #     for i in essential_params:
    #         index += 1
    #         params = params + str(i)
    #         if index != len(essential_params):
    #             params = params + '!^￥^@'
    #     for i in range(start_num, len(unessential_params)+1):
    #         for j in list(combinations(unessential_params, i)):
    #             data.append(j)
    #     print(data)
    #     for i in data:
    #         result = params
    #         for j in i:
    #             result = result + '!^￥^@'
    #             result = result + str(j)
    #         data1 = result.split('!^￥^@')
    #         result = {}
    #         for k in data1:
    #             data2 = k.split('=')
    #             result[data2[0]] = data2[1]
    #         results.append(result)
    #         print(result)
    #     return results

    # 自动生成所有组合方式的参数列表
    @staticmethod
    def auto_params(essential_params, unessential_params, success=True):
        data = []
        results = []
        params = ''
        index = 0
        if len(essential_params) != 0:
            for i in essential_params:
                index += 1
                params = params + str(i)
                if index != len(essential_params):
                    params = params + '!^￥^@'
        for i in unessential_params:
            data.append(i)
        for i in data:
            result = params
            if params != '':
                result = result + '!^￥^@'
            result = result + str(i)
            data1 = result.split('!^￥^@')
            result = {}
            for j in data1:
                data2 = j.split('=')
                result[data2[0]] = data2[1]
            results.append(result)
        return results

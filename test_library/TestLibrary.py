import uuid
import random
import time
import xlwt
import math
from itertools import combinations


class TestLibrary(object):

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

    @staticmethod
    def get_car_models(**kwargs):
        data = {}
        for k, v in kwargs.items():
            if k in ('car_brand', 'car_series', 'car_scale', 'car_model', 'is_car_model',
                     'page_num', 'page_size'):
                data[k] = v
        return data

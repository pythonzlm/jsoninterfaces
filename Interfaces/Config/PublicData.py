#encoding=utf-8
import os
baseDir = os.path.dirname(os.path.dirname(__file__))
file_path = baseDir+"\\TestData\\inter_test_data.xlsx"

API_apiName = 2    #接口名称
API_requestUrl = 3      #请求url
API_requestMothod = 4   #请求方法
API_paramsType = 5      #参数类型
API_apiTestCaseFileName = 6   #测试用例名称
API_active = 7          #用例是否执行标识

CASE_requestData = 1    #请求的数据
CASE_relyData = 2       #请求依赖上的上游响应数据
CASE_responseCode = 3    #请求返回状态码
CASE_responseData = 4    #请求响应类容
CASE_dataStore = 5      #数据存储
CASE_checkPoint = 6     #请求返回内容检查点
CASE_active = 7        #用例是否执行标识
CASE_status = 8        #执行结果状态
CASE_errorInfo = 9     #执行结果错误信息
# 存储请求参数里面依赖数据
REQUEST_DATA = {}
# 存储响应对象中的依赖数据
RESPONSE_DATA = {}
#encoding=utf-8
import requests
import json

class HttpClient(object):
    def __init__(self):
        pass
    def request(self,requestMethod,requestUrl,paramType,requestData=None,headers=None,cookies=None):
        if requestMethod.lower()=="post":
            
            if paramType=="form":
                #requestDataDict = json.loads(json.dumps(eval(requestData)))
                #for i,j in requestDataDict.items():
                    #if type(j) is list:
                        #requestDataDict[i]=j.append()
                response = self.__post(url=requestUrl,data=json.dumps(eval(requestData)),headers=headers,cookies=cookies)

                return response
            elif paramType=="json":
                response = self.__post(url=requestUrl,json=json.dumps(eval(requestData)),headers=headers,cookies=cookies)
                return response
        elif requestMethod.lower()=="get":

            if paramType=="url":
                print type(json.loads(json.dumps(eval(requestData))))
                print "requestdatac:",requestData
                requestDatas = "".join(json.loads(json.dumps(eval(requestData))).keys())+"="
                a= json.loads(json.dumps(eval(requestData)))
                print "values:",a[requestDatas.strip("=")]
                print type(a[requestDatas.strip("=")])
                if type(a[requestDatas.strip("=")]) is list:

                    for i in range(len(a[requestDatas.strip("=")])):
                        if i<len(a[requestDatas.strip("=")])-1:

                            requestDatas+=str(a[requestDatas.strip("=")][i])+','
                        else:
                            requestDatas += str(a[requestDatas.strip("=")][i])
                print "requestdatas:",requestDatas

                request_Url = "%s%s"%(requestUrl,requestDatas)

                response = self.__get(url = request_Url,headers=headers,cookies=cookies)
                return response
            elif paramType=="params":
                response=self.__get(url=requestUrl+requestData,headers=headers,cookies=cookies)
                return response
                print "response:",response
        elif requestMethod.lower()=="put":
            if paramType=="form":
                response = self.__put(url=requestUrl,data=json.dumps(eval(requestData)),headers=headers,cookies=cookies)
                return response
                print "putresponse:",response

    def __post(self,url,data=None,json=None,**kwargs):
        response = requests.post(url=url,data=data,json=json)
        return response

    def __get(self,url,params=None,**kwargs):
        response = requests.get(url=url,params=params)
        return response
    def __put(self,url,data=None,**kwargs):
        response = requests.put(url=url,data=data)
        return response

if __name__=="__main__":
    hc = HttpClient()
    res = hc.request("post","http://39.106.41.11:8080/register/","form",'{"username":"lilysdd12","password":"lily12323","email":"lily@qq.com"}')
    #列出所有res的参数
    print (dir(res))





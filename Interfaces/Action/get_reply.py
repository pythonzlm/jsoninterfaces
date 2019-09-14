#encoding=utf-8
from Config.PublicData import RESPONSE_DATA,REQUEST_DATA
from Utils.md5_encrypt import md5_Encrypt
from data_store import *
class GetKey(object):
    def __init__(self):
        pass
    #where:0,表示没有依赖数据
    #where：1，表示有依赖数据源来自请求参数，说明应该去REQUEST_DATA获取值
    #where:2，表示有依赖数据源来自响应数据，说明应该去RESPONSE_DATA获取值
    @classmethod
    def get(cls,datasource,relydata):
        data = datasource.copy()



        for key,value in relydata.items():
            if key=="request":
           #从REQUEST_DATA获取值
           #{"request":{"username":"用户注册->1","password":"用户注册->1"}}
                for k,v in value.items():
                    interfaceName,case_id=v.split("->")
                    #interfaceName：用户注册 ，case_id:1
                    #data[k]=REQUEST_DATA[interfaceName.decode("utf-8")][case_id][k]
                    val=REQUEST_DATA[interfaceName][case_id][k]

                    if k=="password":
                        data[k]=md5_Encrypt(val)
                    else:
                        data[k]=val

            elif key=="response":
                for k,v in value.items():
                    if type(v)is dict:
                        for i,j in v.items():
                            print "i:",i
                            print "j:",j
                            lists=[]
                            interfaceName, case_id = j.split("->")
                            if i not in RESPONSE_DATA[interfaceName][case_id].keys():
                                if i in RESPONSE_DATA[interfaceName][case_id]['data'][0].keys():
                                    lists.append(RESPONSE_DATA[interfaceName][case_id]['data'][0][i])
                                    data[k] = lists
                                    print "value:",RESPONSE_DATA[interfaceName][case_id]['data'][0][i]
                                    print "lists:",lists
                                    print "K:",{k:data[k]}

                    else:
                       interfaceName,case_id=v.split("->")
                       #print interfaceName,case_id
                       #print RESPONSE_DATA

                           #
                       #else:
                       if k not in RESPONSE_DATA[interfaceName][case_id].keys():
                            if k in RESPONSE_DATA[interfaceName][case_id]['data'][0].keys():
                                 datas=RESPONSE_DATA[interfaceName][case_id]['data'][0][k]
                                 if type(data[k]) is list:
                                       data[k].append(datas)
                                 else:
                                   data[k] = datas
                                   print "data:", {k: data[k]}

                            #for i, j in data.items():
                                #if type(j) is list:
                                    #j.append(data[k])
                                #print "datas:",{k:j}
                       else:
                              data[k] = RESPONSE_DATA[interfaceName][case_id][k]
                              print "data1:", data




        return data
if __name__ == '__main__':
#    datasources = {"username":"","password":""}
   # relydatas = {"request":{"username":"register->1","password":"register->1"}}
    datasources = {"userid":"", "token": "", "title":"testtitle", "content":"testcontent"}
    relydatas={"response":{"userid":"login->1","token":"login->1"}}
    print GetKey.get(datasources, relydatas)




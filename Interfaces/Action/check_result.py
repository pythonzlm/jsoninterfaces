#encoding=utf-8
import re
class CheckResult(object):
    def __init__(self):
        pass
    @classmethod
    def check(cls,responseobj,checkpoint):
        {"code":"00","userid":{"value":"\w+"}}
        errorkey={}
        for key,value in checkpoint.items():
            if isinstance(value,(str,unicode)):
                # 说明是等值校验
                if responseobj[key]!=value:
                    errorkey[key]=responseobj[key]
            #说明需要通过正则表达式校验
            elif isinstance(value,dict):
                sourcedata = responseobj[key]  #接口返回的真实值
                if value.has_key("value"):
                    regStr = value["value"]
                    rg = re.match(regStr,"%s"%sourcedata).group()
                    if not rg:
                        errorkey[key]=sourcedata
                elif value.has_key("type"):
                    #说明是校验数据类型
                    types = value["type"]
                    if types=="N":
                        #说明是整型
                        if not isinstance(sourcedata,(int,long)):
                            errorkey[key]=sourcedata
        return errorkey

if __name__ == '__main__':
    responseobj = {"code":"01", "userid":12, "id":"12"}
    checkpoint = {"code": "00", "userid":{"type":"N"}, "id":{"value":"\d+"}}
    print CheckResult.check(responseobj, checkpoint)
from pandas.io.json import json_normalize
import pandas as pd
import json
import time
from Utils.ParseExcel import *
from Config.PublicData import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

pe = ParseExcel("e:\\test\\Interfaces\\TestData\\test_data.xlsx")

data_str = open('c:\\usermanager.json').read()
data_dict=json.loads(data_str)
#print(data_dict)
#df = json_normalize(data_dict)
#print(df)
with open('d:\\aaa.txt','w') as e:
    for k,v in data_dict.items():
         if k =='requests':
             #print(k)
             #print(data_dict[k])
             for i in data_dict[k]:
                 e.write(json.dumps(i))
                 e.write('\n')
with open('d:\\aaa.txt','r') as f:
    for i in f.readlines():
         #print(type(i))
         #print(i)
         b=json.loads(i)
         #print(type(b))
         rowNum=0
         pe.set_sheet_by_index(0)
         for key in b.keys():
             rowNum+=1
             if key =='url'or key=='method'or key=='name':
                 print b[key]
                 pe.write_cell_content(row_no=rowNum+8,col_no=API_requestUrl,content="%s"%b['url'])
                 pe.write_cell_content(row_no=rowNum + 8, col_no=API_requestMothod,content="%s" % b['method'])
                 pe.write_cell_content(row_no=rowNum + 8, col_no=API_apiName, content="%s" % b['name'])
             if key == 'rawModeData' and b[key]:
                  print b[key]
                  pe.set_sheet_by_name(u"添加用户").decode('utf-8')
                  pe.write_cell_content(row_no=rowNum + 1,col_no=CASE_requestData,content="%s"%b['rawModeData'])
                  #pe.set_sheet_by_name(API_apiName)
                  #pe.write_cell_content(row_no=rowNum + 1, col_no=CASE_requestData, content="%s" % b['rawModeData'])
                  """
             elif key=='headerData' and b[key]:
                 for i in b[key]:
                     if i["key"]=='token':
                         print i["value"]
             """






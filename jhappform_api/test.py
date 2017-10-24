import json


# josn 字符串
ls = '''{
        "name": "case1",
        "expect": "0",
        "casfile": "access_tokne",
        "relese": "6.3.26",
        "gui": "true",
        "ncpu": "2",
        "project": "pro1",
        "jobname": "Fluent01",
        "datfile":"datfile",
        "duatltimestep":"duatltimestep",
        "timesetp":"timesetp",
        "iteration":"iteration",
        "autosavesetp":"autosavesetp",
        "version":"version",
        "priority":"priority"



        }'''

# json字符串转字典
print(type(ls))

fp = file('test.txt', 'r')

print(json.())

print(json.loads(ls))
print(type(json.loads(ls)))

# s = []
# for i in ls.keys():
#     s.append(ls[i] + ":" + i)

# str = ""
# for i in range(len(s)):
#     if ls.keys() != 'version':
#         str += "," + s[i]

# print(str)

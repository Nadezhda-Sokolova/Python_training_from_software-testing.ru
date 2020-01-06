import json

# f = open("/Users/nadezdavolkova/Python_for_testers_course/Practice/config.json")
# try:
#     res = json.load(f)
# except ValueError as ex:
#     print(ex)
#     res={}
# finally:
#     f.close()
#
# print(res)

with open("/Users/nadezdavolkova/Python_for_testers_course/Practice/config.json") as f:
    try:
        res = json.load(f)
    except ValueError as ex:
        print(ex)
        res={}

print(res)
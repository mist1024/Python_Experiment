info= {"stu01":"张三","stu02":"李四","stu03":"王五"}
print(info)
print (info["stu01"])
print(info.get("stu04"))
print("stu03"in info)
info["stu02"]="”李四四”"
print(info)
info["stu04"]="赵六"
print(info)
del info["stu04"]

info.pop("stu03")
print(info)
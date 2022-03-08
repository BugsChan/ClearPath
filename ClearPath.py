
#   Powered by Chen Ziwei at 2022/03/08.
#   Copyleft.
#   陈子为 创作于 2022/03/08 。
#   可自由拷贝和转载。



import sys, os
import time
import shutil

#os.stat
#sys.argv

path = sys.argv[1]
endTime = ""
ensure = False

if sys.argv[1] == "--help":
    print("""
    输入命令行：
    python3 ClearPath.py path endTime ensure
    path : 目录
    endTime : 删掉该目录中所有创建迟于endTime的文件和文件夹 格式为 YEAR-MONTH-DAY
    ensure : 删除文件之前是否给予用户选择权 (yes or no) 可以不加这个参数
    -------------------------
    例如： python3 ClearPath.py . 2021-01-01
    注意：这行代码极有可能把 ClearPath.py 删掉
    
    ---------------------------------English---------------------------------------
    Input in command line:
    python3 ClearPath.py path endTime ensure
    path: The dictionary you want to clear
    endTime: Files and dictionaries which created later than endTime will be removed 
    | You should write endTime like "YEAR-MONTH-DAY"
    ensure: If the program will give you the power to ignore any file or dictionary (Use yes or no) 
    | You can ignore it in the command line
    --------------------------
    You can input like:  python3 ClearPath.py . 2021-01-01
    Attention: These codes will make the program remove itself.
    
    -----------------Copyrite----------------
    Powered by Chen Ziwei at 2022/03/08.
    Copyleft.
    陈子为 创作于 2022/03/08 。
    可自由拷贝和转载。
    
    """)
    exit(0)
else:
    endTime = sys.argv[2]
    ensure = False if (len(sys.argv) < 4 or sys.argv[3] == "no") else True
    print("""
    Path: %s
    endTime: %s
    Ensure to clear ...
    """ % (path, endTime))
    time.sleep(3)


#-----------------------------------------
etms = endTime.split("-")
tm_tuple = (int(etms[0]), int(etms[1]), int(etms[2]), 0, 0, 0, 0, 0, 0)
#-----------------------------------------


endTime = time.mktime(tm_tuple)
totleScan = 0
totleRm = 0


for home, dirs, files in os.walk(path):
    for each_file in files:
        each_file = home + "\\" + each_file
        ctime = os.stat(each_file).st_ctime
        totleScan += 1
        print("\r Totle scan: %d | Totle remove %d" % (totleScan, totleRm))
        if ctime > endTime and (not ensure or input("RM %s (y or n)" % each_file) == "y"):
            os.remove(each_file)
            print("RM: %s" % each_file)
            totleRm += 1
            print("\b Totle scan: %d | Totle remove %d" % (totleScan, totleRm))
    
    for each_dir in dirs:
        each_dir = home + "\\" + each_dir
        ctime = os.stat(each_dir).st_ctime
        totleScan += 1
        print("\b Totle scan: %d | Totle remove %d" % (totleScan, totleRm))
        if ctime > endTime and (not ensure or input("RM %s (y or n)" % each_file) == "y"):
            shutil.rmtree(each_dir)
            print("RM: %s" % each_dir)
            totleRm += 1
            print("\b Totle scan: %d | Totle remove %d" % (totleScan, totleRm))


print("""
Program exit.
""")
import os

def mkdir(dname):
    dname = "./test/" + dname
    os.mkdir(dname)

def touch(fname):
    fname = "./test/" + fname
    open(fname, "w+").close()

if __name__ == "__main__":
    suffixs = ("doc", "docx", "xls", "xlsx", "ppt", "pptx", "dll", "so", "txt", "flv", "mp3", "mp4")
    for i in range(1, 10):
        mkdir("dir%d" % i)
        for each in suffixs:
            touch("test%d.%s" % (i, each))
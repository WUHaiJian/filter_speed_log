# -*- coding: cp936 -*-
import os
#import msvcrt
import threading

log_file = 'LogFilter'
find_0 = "onAcquired(6), vendorCode(1002"
find_1 = "onAcquired(0)"
find_2 = "onAuthenticated(fid"

flag_0 = 0
flag_1 = 0
flag_2 = 0

line_0 = ''
line_1 = ''
line_2 = ''

fd = 0
speed_log = 'filter_speed_log.txt'
f_log = 0

def count_speed_line(line):
    global flag_0
    global flag_1
    global flag_2
    global line_0
    global line_1
    global line_2
    

    if find_0 in line:
        flag_0 = 1
        line_0 = line
    elif find_1 in line:
        if flag_0 != 1:
            flag_0 = 0
            line_0 = ''
            flag_1 = 0
            line_1 = ''
        flag_1 = 1
        line_1 = line
    elif find_2 in line:
        if flag_0 != 1 or flag_1 != 1:
            flag_0 = 0
            line_0 = ''
            flag_1 = 0
            line_1 = ''
            flag_2 = 0
            line_2 = ''
        flag_2 = 1
        line_2 = line

    if flag_0 and flag_1 and flag_2:
        global f_log
        print line_0
        print line_1
        print line_2
        f_log.writelines(str(line_0))
        f_log.writelines(str(line_1))
        f_log.writelines(str(line_2))
        flag_0 = 0
        flag_1 = 0
        flag_2 = 0
        
        

    
       
def search_speed_log():
    dir = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(dir)
    for file in files:
        if log_file in file:
            path = os.path.join('%s\%s' % (dir, file))
            global fd
            fd = open(path)
            if fd != 0:
                for line in fd.readlines():
                    count_speed_line(line)
                fd.close()
	print "Complete filter Speed log!"
                    
     
class speed_thread(threading.Thread):
    def run(self):
        global f_log
        f_log = open(speed_log, 'w+')
        search_speed_log()
        f_log.close()
        

def main():
    #t1 = frr_thread()
    #t2 = far_thread()
    #t1.start()
    #t2.start()
    #t1.join()
    #t2.join()  
    #log_output()
    #fd.close()
    t3 = speed_thread()
    t3.start()
    t3.join()


if __name__ == '__main__':
    main()




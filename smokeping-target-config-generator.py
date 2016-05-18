import re
for line in open("target_IP_list.txt"):  
    print ('++' + ' ' + line.replace('.','_'))
    print ('menu = ' + line.replace('.','_'))
    print ('title = ' + line.replace('.','_'))
    print ('host = ' + line)
    print ('#alerts = someloss')
    print ('\n');

# -*- coding: utf-8 -*-
#!/usr/bin/python
#Udacity提供的字幕和对应的文件名不太一样
#这个脚本用来改当前目录下字幕文件的名字
import os
for (dirname, dirs, files) in os.walk('.'):
    for file in files:
        if file.endswith('.srt'):
            parts = file.split(' ')
            new_name = ''.join(parts[:3])
            if new_name.endswith('.srt'):
                pass
            else:
                new_name += '_'
                new_name += '_'.join(parts[3:])
            os.system('mv "' + file + '" ' + new_name)
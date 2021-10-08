#!/usr/bin/env python3
import os
import time

count = 0
while (count < 99999):
    count = count + 1
    for k in range(20):
        for j in range(5):
            for i in range(1,365*1 + 1):
                d = str(j) + ' day ago'
                with open('text.txt', 'a') as file:
                    file.write(d)
                os.system('git add .')
                os.system('git commit --date="' + d + '" -m "Initial Commit"')
            os.system('git push -u origin main')
            os.system('clear')
            time.sleep(60)
        os.system('git gc; git repack -Ad')
        os.system('rm text.txt')
        os.system('touch text.txt')
        os.system('clear')
        time.sleep(60)
    os.system('git fsck; git gc --prune=now')
    time.sleep(60)

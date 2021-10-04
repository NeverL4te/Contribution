import os
import time

count = 0
while (count < 99999):
    count = count + 1
    for k in range(20):
        for i in range(5):
            for j in range(1,365*1 + 1):
                d = str(i) + ' i'
                with open('text.txt', 'a') as file:
                    file.write(d)
                os.system('git add .')
                os.system('git commit --date="' + d + '" -m "Initial Commit"')
            os.system('git push -u origin main')
            os.system('rm text.txt')
            os.system('touch text.txt')
            os.system('clear')
            time.sleep(40)
        os.system('git gc; git repack -Ad')
        os.system('clear')
        time.sleep(40)
    os.system('git fsck; git gc --prune=now')
    time.sleep(40)

import os
import time

count = 0
while (count < 99999):
    count = count + 1
    for i in range(5):
        for j in range(1,365*1 + 1):
            d = str(i) + ' day ago'
            with open('text.txt', 'a') as file:
                file.write(d)
            os.system('git add .')
            os.system('git commit --date="' + d + '" -m "Initial Commit"')
        os.system('git push -u origin main')
        os.system('rm text.txt')
        os.system('touch text.txt')
        os.system('clear')
        time.sleep(80)
    os.system('git prune; git repack -d')
    os.system('clear')
    time.sleep(80)

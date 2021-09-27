import os
import time

count = 0
while (count < 100):
    count = count + 1
    for i in range(1,365*1 + 1):
        d = str(i) + ' day ago'
        with open('text.txt', 'a') as file:
            file.write(d)
        os.system('git add .')
        os.system('git commit --date="' + d + '" -m "Initial Commit"')
    os.system('git push -u origin main')
    os.system('clear')
    time.sleep(15)
os.system('git gc --prune=now')
os.system('rm text.txt')
os.system('touch text.txt')

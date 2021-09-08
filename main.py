import os

for i in range(1,365*2 + 1):
    d = str(i) + ' day ago'
    with open('text.txt', 'a') as file:
        file.write(d)
    os.system('git add .')
    os.system('git commit --date="' + d + '" -m "Initial Commit"')

os.system('git push -u origin main')

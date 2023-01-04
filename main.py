import os
x = int(input("How many times do you want to commit? \n"))
y = input("Auto git push when commited? (y/n) \n")

for i in range(x):
	os.system(f'git commit --allow-empty -m "Commit {i} of {ip}"')	
print("Commited " + str(ip) + " times")
if y == "y":
	os.system('git push')

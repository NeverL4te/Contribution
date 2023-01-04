import os
x = int(input("How many times do you want to commit? \n"))
for i in range(x):
	os.system(f'git commit --allow-empty -m "Commit {i} of {x}"')
print("Commited " + str(x) + " times")
	os.system('git push')

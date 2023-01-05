#!/usr/bin/env python
import os
x = int(input("How many times do you want to commit? \n"))
for i in range(x):
	os.system(f'git commit --allow-empty -m "Initial Commit"')
	print(f"Commited {i} of {x}")
os.system('git push;clear')

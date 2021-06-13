#! /usr/bin/python3

# script renames files

# importing os module
import os
  
path = os.chdir("/home/kali/Downloads/MD tax")       # path to file 

value = 1
for file in os.listdir(path):
	new_file_name = "tax{}.pdf".format(value)      # place wanted name in "" 
	os.rename( file, new_file_name) 
	
	value = value + 1


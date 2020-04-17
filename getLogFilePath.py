from array import *

filepath = '/root/Desktop/output.txt'

#indexes value
quote_index = 0
slash_index = 1
alpha_numeric = 2

#print("\"ismail")

#2D list 
# -1 mean nothing
table = [[1, -1, -1], [-1, 2, -1], [-1, -1, 3], [4, 2, 3]]
path_list = [] #to store table paths

with open(filepath) as fp:
   line = fp.readline()
   while line:
	line = fp.readline() #read line by line from file
        #print(line)
	if(("(No such file or directory)" in line) == False):
		
		
		temp_string = ""
		flag = 0
		current_index_row = 0
		current_index_col = 0
		count = 0
		special_chFlag = 0 #special character flag to redefine the state 3
		for i in range(len(line)):
			if(line[i] == "\""):
				current_index_row = table[current_index_row][quote_index]
				temp_string = temp_string + "\""
				count = i + 1
				#print(temp_string)
						
				while(True):
					#print(current_index_row, ":" ,current_index_col)
					if(line[count] == "\""):
						if(current_index_row == 4):
							flag = 1
			 				break
						current_index_col = quote_index						
						current_index_row = table[current_index_row][current_index_col]
						temp_string = temp_string + "\""
						#print(temp_string)
						if(current_index_row == -1):
							break
											
					elif( (line[count].isalpha() or line[count].isdigit()) and special_chFlag == 0 ):
						special_chFlag = 1 
						# now we allow special character to come 						
						if(current_index_row == 4):
							flag = 1
			 				break						
						current_index_col = alpha_numeric
						current_index_row = table[current_index_row][current_index_col]
						temp_string = temp_string + line[count]
						#print(temp_string)
						
												
						if(current_index_row == -1):
							break
					#redundant due to special character other than backslash because it is not allowed as it represent the directory and linux also do not allow it for rename 						
					elif( (line[count].isalpha() or line[count].isdigit() or line[count] in "`~!@#$%^&*()_+=-[]{}|;:'\"/?.>,<") and special_chFlag == 1 ):
												
						if(current_index_row == 4):
							flag = 1
			 				break						
						current_index_col = alpha_numeric
						current_index_row = table[current_index_row][current_index_col]
						temp_string = temp_string + line[count]
						#print(temp_string)
						
												
						if(current_index_row == -1):
							break
										

					elif(line[count] == "/"):
						if(current_index_row == 4):
							flag = 1
			 				break
						current_index_col = slash_index
						current_index_row = table[current_index_row][current_index_col]
						temp_string = temp_string + "/"
						#print(temp_string)
												
						if(current_index_row == -1):
							break
					
					count = count + 1
			if(flag == 1):
				break
			

		if(current_index_row == 4 and flag == 1 and len(temp_string)>3 ):
			#print(temp_string) #print paths
			path_list.append(temp_string) #store paths in a list
			

print("Before Number of Paths: ", len(path_list))
print("----------------------------------------")
print("Remove Redundancy")
print("----------------------------------------")
path_list = list(set(path_list))		
print("After Number of Paths: ", len(path_list))
print("----------------------------------------")
for i in range(len(path_list)):	
	print(path_list[i])



#creating, reading and appending external files

#1. Find your folder you want to save the file in
#2. Copy the path to the folder
#3. The text doesn't appear until you close the file

#writing to a file
#if the file does not exist it will be created

write_file=open(r'#paste your path here - add the name of the file to the end of the path','w')
write_file.write("This is the first sentence in our file.")
write_file.close()

#append a file
#this adds text to a file without removing the old text

append_file=open(r'#paste the path here again','a')
append_file.write(" This is our second sentence in our file.")
append_file.close()

#context manager
#Don't need to use the close command

with open((r'#paste the path here again','a')as append_file:
    append_file.write("\nThis is our third sentence in our file, on a new line")

#read contents of file

with open(r'#paste the path here again','r')as read_file:
    print(read_file.read())




#run the code again and test



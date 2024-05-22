#creating, reading and appending external files

#1. Find your folder you want to save the file in
#2. Copy the path to the folder
#3. The text doesn't appear until you close the file

#writing to a file
#if the file does not exist it will be created

write_file=open(r'#paste your path here - add the name of the file to the end of the path','w')
write_file.write("This is the first sentence in our file.")
write_file.close()

#run the code and test
#has the file been created?
#has the text been written to the file?

#Move to externalFile 002.py

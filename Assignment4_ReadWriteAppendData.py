#Program to take input from user and write to the file and also append additional text
inp_text = str(input("Enter text to write to the file: "))
file = open('output.txt','w')
file.write(inp_text)
print("Data Successfully written to output.txt.")
file.close()
app_text = str(input("Enter additional text to append : "))
file = open('output.txt','a')
file.write("\n"+app_text)
print("Data Successfully appended.")
file.close()

#read the file content and display
file1 = open('output.txt','r')
read_file = file1.read()
print(read_file)
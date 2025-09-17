try:
    file1 = open('Sample.txt', 'r')
    read_lines = file1.readlines()
    line_count = len(read_lines)
    j=0
    while j<line_count:
        print("Line",j+1,":",read_lines[j])
        j=j+1
    file1.close()
except FileNotFoundError:
    print("The file Sample.txt was not found.")
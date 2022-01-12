import os

with open("220.txt", "r") as input:
    with open("temp1.txt", "w") as output:
        # iterate all lines from file
        for line in input:
            # if substring contain in a line then don't write it
            if "D" not in line.strip("\n"):
                output.write(line)
file.close




import os

with open("temp1.txt", "r") as input:
    with open("temp2.txt", "w") as output:
        # iterate all lines from file
        for line in input:
            # if substring contain in a line then don't write it
            if "s" not in line.strip("\n"):
                output.write(line)
file.close





with open(r"temp2.txt", 'r+') as fp:
    # read an store all lines into list
    lines = fp.readlines()
    # move file pointer to the beginning of a file
    fp.seek(0)
    # truncate the file
    fp.truncate()

    # start writing lines except the first line
    # lines[1:] from line 2 to last line
    fp.writelines(lines[28:])


import os

with open("temp2.txt", "r") as input:
    with open("temp1.txt", "w") as output:
        # iterate all lines from file
        for line in input:
            # if substring contain in a line then don't write it
            if line.split():
                output.write(line)
file.close

# list to store file lines
lines = []
# read file
with open(r"temp1.txt", 'r') as fp:
    # read an store all lines into list
    lines = fp.readlines()

# Write file
with open(r"temp1.txt", 'w') as fp:
    # iterate each line
    for number, line in enumerate(lines):
        # delete line 5 and 8. or pass any Nth line you want to remove
        # note list index starts from 0
        if number not in range(195,222):
            fp.write(line)

fp = file('temp1.txt')
s = fp.read()
fp.close()
a = s.split('\n')
a.insert(195,'          425.0')
s = '\n'.join(a)
fp = file('220.txt','w')
fp.write(s)
fp.close()


# For the Lich King!

# Yingning
# 2021-12-24





# Delete title
import os

with open("890.txt", "r") as input:
    with open("temp1.txt", "w") as output:
        for line in input:
            if "D" not in line.strip("\n"):
                output.write(line)
file.close
import os
with open("temp1.txt", "r") as input:
    with open("temp2.txt", "w") as output:
        for line in input:
            if "s" not in line.strip("\n"):
                output.write(line)
file.close
with open(r"temp2.txt", 'r+') as fp:
    lines = fp.readlines()
    fp.seek(0)
    fp.truncate()
    fp.writelines(lines[18:])

# Delete blank
import os
with open("temp2.txt", "r") as input:
    with open("890.txt", "w") as output:
        # iterate all lines from file
        for line in input:
            # if substring contain in a line then don't write it
            if line.split():
                output.write(line)
file.close





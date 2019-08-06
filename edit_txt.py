# imports
import os

# specify directory of files
path = 'samples'
fileList = os.listdir('samples')

# create new directory for writing files
newPath = 'txt/'

if not os.path.exists(newPath):
    os.makedirs(newPath)

counter = 0

# loop through every file in the directory
for txt in fileList:

    # if the file ends with .txt
    if txt.endswith('.txt'):

        # open the file for writing
        text = open(os.path.join(path, txt), 'r')

        # create new file name
        newFileName = str(counter) + '.txt'

        # create new file to write to
        newText = open(os.path.join(newPath, txt), 'w')

        # file processing
        try:
            # return a list of all lines
            lines = text.readlines()
            
            # create a list of new lines
            newLines = []

            # iterate through each line
            for j, line in enumerate(lines, 0):
                
                # create a list of nums from current line  
                nums = line.split(',')

                # create a list of new nums
                newNums = [0]

                # convert all nums from strings to floats
                for k, num in enumerate(nums, 0):
                    nums[k] = float(nums[k])

                # convert topleft_x to center_x
                newNums.append(((nums[0] + nums[2]) / 2.0) / 800.0)

                # convert topleft_y to center_y
                newNums.append(((nums[1] + nums[3]) / 2.0) / 600.0)

                # convert botleft_x to width
                newNums.append((nums[2] - nums[0] + 1.0) / 800.0)

                # convert botleft_y to height
                newNums.append((nums[3] - nums[1] + 1.0) / 600.0)

                # write new line to text file
                for k, newNum in enumerate(newNums, 0):
                    newText.write(str(newNum) + ' ')
                newText.write(os.linesep)
        
        # close the files
        finally:
            text.close()
            newText.close()
        
        counter += 1
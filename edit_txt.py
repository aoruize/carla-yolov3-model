# imports
import os

# specify directory of files
path = 'test'
fileList = os.listdir('test')

# create new directory for writing files
newPath = 'test/txt/'

if not os.path.exists(newPath):
    os.makedirs(newPath)


# loop through every file in the directory
for i, txt in enumerate(fileList):

    # if the file ends with .txt
    if txt.endswith('.txt'):

        # open the file for writing
        text = open(os.path.join(path, txt), 'r')

        # create new file name
        newFileName = str(i) + '.txt'

        # create new file to write to
        newText = open(os.path.join(newPath, newFileName), 'w')

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
                newNums.append((nums[0] + nums[2]) / 2.0)

                # convert topleft_y to center_y
                newNums.append((nums[1] + nums[3]) / 2.0)

                # convert botleft_x to width
                newNums.append(nums[2] - nums[0] + 1.0)

                # convert botleft_y to height
                newNums.append(nums[3] - nums[1] + 1.0)

                # write new line to text file
                for k, newNum in enumerate(newNums, 0):
                    newText.write(str(newNum) + ' ')
                newText.write(os.linesep)

        # close the files
        finally:
            text.close()
            newText.close()
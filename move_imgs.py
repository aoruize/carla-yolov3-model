import os
import shutil

path = 'samples'
newPath = 'txt'
imgList = os.listdir('samples')
counter = 0

for img in imgList:
    if img.endswith('.png'):
        
        shutil.copy(os.path.join(path, img), (os.path.join(newPath, img)))
        
        counter += 1
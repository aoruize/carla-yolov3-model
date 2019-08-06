import glob, os

def rename(dir, pattern, titlePattern):
    for i, pathAndFilename in enumerate(glob.iglob(os.path.join(dir, pattern))):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        os.rename(pathAndFilename, 
                  os.path.join(dir, str(i) + ext))


rename(r'test', r'*.txt', r'new(%s)')
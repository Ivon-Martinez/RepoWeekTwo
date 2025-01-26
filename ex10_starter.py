import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']
print(hdir)

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')
print(pattern)

# TODO: Use the glob.glob() function to obtain the list of filenames
list_fileName = glob.glob(pattern)
print(list_fileName)

# TODO: use os.path.getsize to find each file's size
for file in list_fileName:
    files_size = os.path.getsize(file)
    print(f"File: {file}, Size: {files_size} bytes")

# TODO: Add a test to only display files that are not zero length
for file in list_fileName:
    if os.path.getsize(file) != 0:
        files_size = os.path.getsize(file)
        print(f"File: {file}, Size: {files_size} bytes")


# TODO: Remove the leading directory name(s) from each filename before you print it - 
for file in list_fileName:
    if os.path.getsize(file) != 0:
        files_noneZero = os.path.getsize(file)
        remoVar = os.path.basename(file)
        print(f"File: {remoVar}, Size: {files_noneZero} bytes")


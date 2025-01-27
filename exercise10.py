import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
# This wildcard character(*) will return a list of files or folders with zero or more character matches.
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames
# method 1
files = glob.glob(pattern)
print(files)

# # method 2
for file in glob.glob(pattern):
        print(file)



# TODO: use os.path.getsize to find each file's size
for file in glob.glob(pattern):
    size = os.path.getsize(file)
    print(file, size, "bytes")
#
#
# # TODO: Add a test to only display files that are not zero length
for file in glob.glob(pattern):
    size = os.path.getsize(file) > 0
    print(file)
#
# # TODO: Remove the leading directory name(s) from each filename before you print it -
# # using os.path.basename()
for file in glob.glob(pattern):
    base = os.path.splitext(os.path.basename(file)) [0]
    print(base,)



import os

for root, dirs, files in os.walk(".."):
    abs_root = os.path.abspath(root)
    # print((abs_root))
    if dirs:
        print("Direct")
        for dir_ in dirs:
            print(dir_)

    if files:
        print("files")
        for filename in files:
            print(filename)
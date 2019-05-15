import os

folder = '/Users/imaki/DubaiPictures/' # Destination directory

def rename_files():
    i = 1 # From what number starts to count in the loop

# I use sorted func, because listdir doesn't sort the files
    for file in sorted(os.listdir(folder)):
        dst = "dubai" + str(i) + ".jpg" # Set name and extansion
        src = folder + file
        dst = folder + dst

        os.rename(src, dst) # rename file
        i += 1

rename_files()

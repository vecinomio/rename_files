import os

def rename_files(folder_path):
    i = 1 # From what number starts to count in the loop

    # I use sorted func, because listdir doesn't sort the files
    for file in sorted(os.listdir(folder_path)):
        dst = "pict" + str(i) + ".jpeg" # Set name and extension
        src = folder_path + file
        dst = folder_path + dst

        os.rename(src, dst) # rename file
        i += 1

rename_files('/Users/imaki/Documents/test/') # Argument - path to the files

import os

def rename_files(folder_path):
    i = 1 # From what number starts to count in the loop

    # I use sorted func, because listdir doesn't sort the files
    for file_name in sorted(os.listdir(folder_path)):
        src = folder_path + file_name

        if os.stat(src).st_size > 5242880:
            dst = "sportcar" + str(i) + ".mp4" # Set name and extension
        else:
            dst = "sportcar" + str(i) + ".jpg"

        dst = folder_path + dst

        os.rename(src, dst) # rename file
        i += 1

rename_files('/Users/imaki/Documents/test/') # Argument - path to the files

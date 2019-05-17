import os

def rename_files(folder_path):
    n = 1 # From what number starts to count in the loop

    file_list = os.listdir(folder_path)
    full_list = [os.path.join(folder_path, i) for i in file_list]
    time_sorted_list = sorted(full_list, key=os.path.getctime)

    for file_name in time_sorted_list:
        #src = folder_path + file_name

        if os.stat(file_name).st_size > 5242880: # More than 5Mb
            dst = "sp" + str(n) + ".mp4" # Set name and extension
        else:
            dst = "sp" + str(n) + ".jpg"

        dst = folder_path + dst

        os.rename(file_name, dst) # rename file
        n += 1

rename_files('C:\\Users\\Administrator\\Downloads\\test\\')

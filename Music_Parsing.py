import os
import eyed3

root_dir = "/media/matt/Storage/Music/A Day to Remember"

'''
for dirName, subdirList, fileList in os.walk(root_dir):
    start_index = -1
    for i in range(len(dirName)):
        if dirName[i] == "/":
            start_index = i

    start_index += 1

    print(dirName[start_index:])

    if dirName[start_index + 5] == "-":
       start_index += 7

    print(dirName[start_index:])

    for fname in fileList:
       try:
            x = int(fname[0:2])
            print("\t\t%s" % fname[fname.index(" ") + 1:])
       except:
            None
'''

for dir_name, subdir_list, file_list in os.walk(root_dir):
    for file_name in file_list:
        if file_name.endswith(".mp3"):
            # f = open(dir_name + "/" + file_name, "rb")
            # #f.seek(20, 1)
            # tag_data = f.read(128)
            # print(tag_data)
            track_info = eyed3.Mp3AudioFile(file_name)
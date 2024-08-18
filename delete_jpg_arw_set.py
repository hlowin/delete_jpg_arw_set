import os
import sys

import shutil

import cv2

def delete_jpg_arw_set(dirpath):

  dirpath = dirpath.replace('\\', '/')

  # get files name as list
  file_list = os.listdir(dirpath)

  # extract jpeg files name as list
  jpg_file_list = [file for file in file_list if file.upper().find(".JPG") >= 0]

  # no jpeg file
  if (len(jpg_file_list) == 0):
    print("[ERROR] cannot find any jpeg files")
    return

  # make directry for delete files
  delete_dirpath = dirpath + "/[DELETE]"
  os.makedirs(delete_dirpath, exist_ok=True)

  index = 0
  while True:
    jpeg_filepath = dirpath + "/" + jpg_file_list[index]
    
    image = cv2.imread(jpeg_filepath)

    # resize for display size
    # adjust about XGA size
    height, width, channnel = image.shape
    rate = float(1024) / float(width) 
    image = cv2.resize(image, None, fx=rate, fy=rate, interpolation=cv2.INTER_LANCZOS4)

    cv2.imshow("viewer", image)
    
    # wait any key
    key = cv2.waitKey(0)

    # debug
    # print(key)

    if key == 46:       # next image by ">" key
      index = index + 1
    if key == 44:       # prev image by "<" key
      index = index - 1
    if key == 100:      # delete file by "d" key
      arw_filepath = jpeg_filepath.upper().replace(".JPG", ".ARW")
      shutil.move(jpeg_filepath, delete_dirpath)
      shutil.move(arw_filepath, delete_dirpath)
      index = index + 1
    elif key == 27:     # quit by "esc" key
      break
  
  return

if __name__ == "__main__":
  # get arguments
  args = sys.argv

  # specify current directory in debug mode
  dirpath = "."

  # specify directory path from arguments
  if (len(args) == 2):
    dirpath = args[1]

  delete_jpg_arw_set(dirpath)
    
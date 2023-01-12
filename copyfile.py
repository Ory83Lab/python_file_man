

# import os
# import shutil
# from shutil import SameFileError

# src_folder = r"/Users/orazioconte/Desktop/django-script/manage_file/partenza/static/"
# dst_folder = r"/Users/orazioconte/Desktop/django-script/manage_file/destinazione/static/"

# # printing the contents of the destination folder
# print("Destination folder before copying::", os.listdir(dst_folder))

# # file names
# src_file = src_folder + "base.html"
# dst_file = dst_folder + "base.html"

# try:
#     # copy file
#     shutil.copyfile(src_file, dst_file)
#     # destination folder after copying
#     print("Destination after copying", os.listdir(dst_folder))
# except SameFileError:
#     print("We are trying to copy the same File")
# except IsADirectoryError:
#     print("The destination is a directory")


# =================================================================

# ! OOOK FUNZIONA E COPIA LA DIRECTORY PIù LE SOTTO DIRECTORY CONTENUTE
# ! Questo è il master base principale

import shutil

source_dir = r"/Users/orazioconte/Desktop/django-script/manage_file/partenza/static/"
destination_dir = r"/Users/orazioconte/Desktop/django-script/manage_file/destinazione/static/"
shutil.copytree(source_dir, destination_dir)


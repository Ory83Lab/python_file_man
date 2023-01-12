# ! OOOK FUNZIONA E COPIA LA DIRECTORY PIù LE SOTTO DIRECTORY CONTENUTE
# ! Questo è il master base principale

import shutil

source_dir = r"/Users/orazioconte/Desktop/django-script/manage_file/partenza/static/"
destination_dir = r"/Users/orazioconte/Desktop/django-script/manage_file/destinazione/static/"
shutil.copytree(source_dir, destination_dir)


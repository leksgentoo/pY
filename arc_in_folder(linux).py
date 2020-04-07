#!/usr/bin/env python3

import datetime
import zipfile
import glob

dt = datetime.datetime.today().strftime('%d.%m.%Y--%H.%M')

names = glob.glob('/path')  # path to dir; * for all files
zip_f = zipfile.ZipFile('{}.zip'.format(dt), mode='w', allowZip64=True)
for i in names:
    zip_f.write(i)
zip_f.close()

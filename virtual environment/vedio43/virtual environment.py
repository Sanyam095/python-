# Microsoft Windows [Version 10.0.19045.6466]
# (c) Microsoft Corporation. All rights reserved.

# C:\Users\hp>myenv\Scripts\activate.bat
# The system cannot find the path specified.

# C:\Users\hp>myemv\Scripts\activate.bat

# (myemv) C:\Users\hp>pip install six
# Requirement already satisfied: six in .\myemv\Lib\site-packages (1.17.0)

# [notice] A new release of pip is available: 26.1.1 -> 26.1.2
# [notice] To update, run: python.exe -m pip install --upgrade pip

# (myemv) C:\Users\hp>python.exe -m pip install --upgrade.pip

# [optparse.groups]Usage:[/]
#   C:\Users\hp\myemv\Scripts\python.exe -m pip install \[options] <requirement specifier> \[package-index-options] ...
#   C:\Users\hp\myemv\Scripts\python.exe -m pip install \[options] -r <requirements file> \[package-index-options] ...
#   C:\Users\hp\myemv\Scripts\python.exe -m pip install \[options] [-e] <vcs project url> ...
#   C:\Users\hp\myemv\Scripts\python.exe -m pip install \[options] [-e] <local project path> ...
#   C:\Users\hp\myemv\Scripts\python.exe -m pip install \[options] <archive url/path> ...

# no such option: --upgrade.pip

# (myemv) C:\Users\hp>python
# Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> pip install dateutils
#   File "<python-input-0>", line 1
#     pip install dateutils
#         ^^^^^^^
# SyntaxError: invalid syntax
# >>> exit()

# (myemv) C:\Users\hp>pip install dateutils
# Collecting dateutils
#   Downloading dateutils-0.6.12-py2.py3-none-any.whl.metadata (1.3 kB)
# Requirement already satisfied: python-dateutil in .\myemv\Lib\site-packages (from dateutils) (2.9.0.post0)
# Collecting pytz (from dateutils)
#   Downloading pytz-2026.2-py2.py3-none-any.whl.metadata (22 kB)
# Requirement already satisfied: six>=1.5 in .\myemv\Lib\site-packages (from python-dateutil->dateutils) (1.17.0)
# Downloading dateutils-0.6.12-py2.py3-none-any.whl (5.7 kB)
# Downloading pytz-2026.2-py2.py3-none-any.whl (510 kB)
# Installing collected packages: pytz, dateutils
# Successfully installed dateutils-0.6.12 pytz-2026.2

# [notice] A new release of pip is available: 26.1.1 -> 26.1.2
# [notice] To update, run: python.exe -m pip install --upgrade pip

# (myemv) C:\Users\hp>pip install openpyxl
# Collecting openpyxl
#   Downloading openpyxl-3.1.5-py2.py3-none-any.whl.metadata (2.5 kB)
# Collecting et-xmlfile (from openpyxl)
#   Downloading et_xmlfile-2.0.0-py3-none-any.whl.metadata (2.7 kB)
# Downloading openpyxl-3.1.5-py2.py3-none-any.whl (250 kB)
# Downloading et_xmlfile-2.0.0-py3-none-any.whl (18 kB)
# Installing collected packages: et-xmlfile, openpyxl
# Successfully installed et-xmlfile-2.0.0 openpyxl-3.1.5

# [notice] A new release of pip is available: 26.1.1 -> 26.1.2
# [notice] To update, run: python.exe -m pip install --upgrade pip

# (myemv) C:\Users\hp>pip install pytz
# Requirement already satisfied: pytz in .\myemv\Lib\site-packages (2026.2)

# [notice] A new release of pip is available: 26.1.1 -> 26.1.2
# [notice] To update, run: python.exe -m pip install --upgrade pip

# (myemv) C:\Users\hp>pip install numpy
# Requirement already satisfied: numpy in .\myemv\Lib\site-packages (2.5.0)

# [notice] A new release of pip is available: 26.1.1 -> 26.1.2
# [notice] To update, run: python.exe -m pip install --upgrade pip

# (myemv) C:\Users\hp>pip freeze
# dateutils==0.6.12
# et_xmlfile==2.0.0
# numpy==2.5.0
# openpyxl==3.1.5
# pandas==3.0.3
# python-dateutil==2.9.0.post0
# pytz==2026.2
# six==1.17.0
# tzdata==2026.2

# (myemv) C:\Users\hp>pip freeze > Requirements.txt

# (myemv) C:\Users\hp>deactivate
# C:\Users\hp>myvenv\Scripts\activate.bat

# (myvenv) C:\Users\hp>pip install -r requirements.txt
# Collecting dateutils==0.6.12 (from -r requirements.txt (line 1))
#   Using cached dateutils-0.6.12-py2.py3-none-any.whl.metadata (1.3 kB)
# Collecting et_xmlfile==2.0.0 (from -r requirements.txt (line 2))
#   Using cached et_xmlfile-2.0.0-py3-none-any.whl.metadata (2.7 kB)
# WARNING: Cache entry deserialization failed, entry ignored
# Collecting numpy==2.5.0 (from -r requirements.txt (line 3))
#   Using cached numpy-2.5.0-cp314-cp314-win_amd64.whl.metadata (6.6 kB)
# Collecting openpyxl==3.1.5 (from -r requirements.txt (line 4))
#   Using cached openpyxl-3.1.5-py2.py3-none-any.whl.metadata (2.5 kB)
# WARNING: Cache entry deserialization failed, entry ignored
# Collecting pandas==3.0.3 (from -r requirements.txt (line 5))
#   Using cached pandas-3.0.3-cp314-cp314-win_amd64.whl.metadata (19 kB)
# Collecting python-dateutil==2.9.0.post0 (from -r requirements.txt (line 6))
#   Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
# Collecting pytz==2026.2 (from -r requirements.txt (line 7))
#   Using cached pytz-2026.2-py2.py3-none-any.whl.metadata (22 kB)
# Collecting six==1.17.0 (from -r requirements.txt (line 8))
#   Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
# Collecting tzdata==2026.2 (from -r requirements.txt (line 9))
#   Using cached tzdata-2026.2-py2.py3-none-any.whl.metadata (1.4 kB)
# Using cached dateutils-0.6.12-py2.py3-none-any.whl (5.7 kB)
# Using cached et_xmlfile-2.0.0-py3-none-any.whl (18 kB)
# Using cached numpy-2.5.0-cp314-cp314-win_amd64.whl (12.6 MB)
# Using cached openpyxl-3.1.5-py2.py3-none-any.whl (250 kB)
# Using cached pandas-3.0.3-cp314-cp314-win_amd64.whl (9.9 MB)
# Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
# Using cached pytz-2026.2-py2.py3-none-any.whl (510 kB)
# Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
# Using cached tzdata-2026.2-py2.py3-none-any.whl (349 kB)
# Installing collected packages: pytz, tzdata, six, numpy, et_xmlfile, python-dateutil, openpyxl, pandas, dateutils
# Successfully installed dateutils-0.6.12 et_xmlfile-2.0.0 numpy-2.5.0 openpyxl-3.1.5 pandas-3.0.3 python-dateutil-2.9.0.post0 pytz-2026.2 six-1.17.0 tzdata-2026.2

# [notice] A new release of pip is available: 26.1.1 -> 26.1.2
# [notice] To update, run: python.exe -m pip install --upgrade pip

# (myvenv) C:\Users\hp>deactivate
# C:\Users\hp>
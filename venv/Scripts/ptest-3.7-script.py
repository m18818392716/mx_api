#!D:\software\PycharmProject\APITest\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'ptest==1.9.5','console_scripts','ptest-3.7'
__requires__ = 'ptest==1.9.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('ptest==1.9.5', 'console_scripts', 'ptest-3.7')()
    )

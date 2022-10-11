from cx_Freeze import setup, Executable
import os.path

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

include_files = [os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
                 os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll')]

setup(
    name='gerador de politicas',
    description='interface para geracao de politcas javascript',\
    version='1.0.0',
    options={'build_exe': {'include_files': include_files}},
    executables=[Executable('main.py',
                            targetName='robotZoom.exe',
                            # icon='icon/icon.ico',
                            copyright='Copyright (C) felipesdreis 2022',
                            base='Console' #Win32GUI for interface or Console for CMD
                            )]
)

# to run -> python setup.py build

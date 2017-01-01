# Console Application
from cx_Freeze import setup, Executable

setup(name='AppName 1.9.5',
      version='1.16.9.5',
      description='Description',
      executables = [Executable('main.py')])
#-------------------------------------------------------------------------------
# Tkinter application Python 2.7
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"includes": ["Tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"


setup(  name = "AlgoAnalysis 1B",
        version = "0.1",
        description = "Exercise 1b",
        options = {"build_exe": build_exe_options},
        executables = [Executable("exercise_1b.py", base=base)])

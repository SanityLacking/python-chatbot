import sys
from cx_Freeze import setup, Executable
exe = Executable(
    script="eduhouse_chatbot.py",
    base="Win32GUI",
    )

setup(
    name = "TESTApp",
    version = "0.1",
    description = "An example",
    executables = [exe]
    )

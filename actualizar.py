from os import system
try:
    system('python3 -m pip3 install -U pip3')
    system('python3 -m pip3 install -U matplotlib')
    system('python3 -m pip install -U pip')
    system('python3 -m pip install -U matplotlib')
except:
    system('python -m pip install -U pip')
    system('python -m pip install -U matplotlib')
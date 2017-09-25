#paython_entry should be in sys.paython_entry
#it can be added by appending its path to sys.path or export PYTHONPATH=location_of_python_entry

#Adding __init__.py in packages initialize them as python modules.

print('my_package is being imported')
from my_package.reader import Reader

def myFunc():
    print('Inside my_package')

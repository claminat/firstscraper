import os
import py_compile

pyc_files = []
py_files = []

for root, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.pyc'):
            # print('filename',filename)
            # print('%s%s' % (dirnames,filename))
            pyc_files.append(os.path.join(root, filename))

        # elif filename.endswith('.py'):
        #     print('############################################################################################')
        #     print('filename',filename)
        #     print(os.path.join(root, filename))
        #     py_files.append(os.path.join(root, filename))
        
for py_file in py_files:
        print('############################################################################################')
        print('py_file',py_file)
        # if py_file + 'c' not in pyc_files:
        #     os.remove(py_file)
for pyc_file in pyc_files:
        print('############################################################################################')
        print('pyc_file',pyc_file)
        os.remove(pyc_file)

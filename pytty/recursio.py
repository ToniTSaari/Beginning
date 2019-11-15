import os

dir = os.path.join(os.getcwd(), 'moro.py')

f = open(dir, "w")
f.write("print('Hello world!')")
f.close()

command = dir + " moro.py"
os.system(command)

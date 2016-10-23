import sys
print(sys.float_info)
print(sys.modules)
#print(sys.executable())
print(' %s : %s' % ("sys.version", sys.version))
sorted_sys_modules = ', '.join(sorted(sys.modules.keys()))
print(sorted_sys_modules)

for name in sys.builtin_module_names:
    print(name)

for path in sys.path:
    print(path)


sys.stderr.flush()
sys.stderr.write('This is stderr text1\n')
sys.stdout.write('This is stdout text2\n')

print(dir(sys))

print(dir(sys.path))
print("%s : %s" % ("sys executable is", sys.executable))

#sys.exit(0  )
#sys.exit(1)

print("*****************************************")

import os

files = os.system("ls -l")

files = os.system("ls")


for path in os.listdir("/Users/mona"):
    if os.path.isfile(path):
        print(path)

print("%s: %s" % ("max size is", sys.maxsize))
print("%s: %s" % ("platform is", sys.platform))

if not os.path.exists("test_dir"):
    os.makedirs("test_dir")

os.system("touch test_dir/test.txt")
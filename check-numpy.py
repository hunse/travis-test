import os
import re
import subprocess
import numpy

numpy_root = os.path.dirname(numpy.__file__)
numpy_core = os.path.join(numpy_root, 'core')

core_files = sorted(os.listdir(numpy_core))
print "##### core files #####"
for filename in core_files:
    print filename


process = subprocess.Popen("dpkg --get-selections".split(),
                           stdout=subprocess.PIPE)
output = process.communicate()[0]

print "##### numpy packages #####"
for line in output.split('\n'):
    if line.find("numpy") >= 0:
        print line

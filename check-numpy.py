import os
import re
import subprocess
import numpy

numpy_root = os.path.dirname(numpy.__file__)
print "numpy root:", numpy_root

print
print "##### core files #####"
numpy_core = os.path.join(numpy_root, 'core')
core_files = sorted(os.listdir(numpy_core))
for filename in core_files:
    print filename


print
print "##### numpy packages #####"
process = subprocess.Popen("dpkg --get-selections".split(),
                           stdout=subprocess.PIPE)
output = process.communicate()[0]
for line in output.split('\n'):
    if line.find("numpy") >= 0:
        print line

print
print "##### numpy.show_config() #####"
print numpy.show_config()

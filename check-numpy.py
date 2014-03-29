import os
import numpy

numpy_root = os.path.dirname(numpy.__file__)
numpy_core = os.path.join(numpy_root, 'core')

core_files = sorted(os.listdir(numpy_core))
print "##### core files #####"
for filename in core_files:
    print filename

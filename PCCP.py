import sys
import os

# Import numpy.
try:
    import numpy
except ImportError:
    errMsg = (
        "numpy is required."
        " If you are on Ubuntu you can install it by running"
        " 'sudo apt-get install python-numpy'.")
    raise ImportError(errMsg)

# Import STL_Writer. It should exist in the same directory as this
# file.
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import STL_Writer

def Main():
    print "Main()!"

if "__main__" == __name__:
    Main()

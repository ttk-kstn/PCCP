import sys
import os
import argparse

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
    parser = argparse.ArgumentParser(
        description=("Make STL model of pseudo-cylindrical concave "
                     "polyhedral shell."))
    parser.add_argument("--radius", type=float, default=1.0)
    args = parser.parse_args()

    radius = args.radius
    heights = [0.1] * 20
    N = 12

    angles = numpy.arange(0.0, 1.0, 1.0 / float(N)) * (2.0 * numpy.pi)
    vertices = []
    for lv in range(len(heights) + 1):
        vertices.append([])
        z = numpy.sum(heights[:lv])
        for n in range(N):
            a = angles[n]
            if 1 == lv % 2:
                a += 0.5 / float(N) * 2.0 * numpy.pi
            v = (radius * numpy.cos(a), radius * numpy.sin(a), z)
            vertices[lv].append(v)
    # Connect vertices
    faces = []
    for lv in range(len(heights)):
        twist = lv % 2
        for n in range(N):
            face = [vertices[lv + 0][n],
                    vertices[lv + 0][(n + 1) % N],
                    vertices[lv + 1][(n + twist) % N]]
            faces.append(face)
            face = [vertices[lv + 1][(n + twist + 1) % N],
                    vertices[lv + 1][(n + twist) % N],
                    vertices[lv + 0][(n + 1) % N]]
            faces.append(face)
    # Write STL file.
    fp = open("test.stl", "wb")
    writer = STL_Writer.Binary_STL_Writer(fp)
    writer.add_faces(faces)
    writer.close()

if "__main__" == __name__:
    Main()

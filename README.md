# School Project

This was a school project. We attempted to solve a Rubik's cube using a Lego set and Python.

Since we live in Germany, the comments within the methods are written in German.

The classes found in the files under Robot/Cube/* can be used without a Lego robot.

# Wuerfel

The class Wuerfel models a cube. The colors are stored in a dictionary, and the rotation logic is implemented accordingly.

# Cubesolver

This class takes a Wuerfel object as an argument and solves that cube using the beginner's algorithm. Typically, this method results in around 100 to 200 rotations to solve the entire cube. There is a method to retrieve the list of solving steps.

---

The other classes were intended for the Lego robot and didn't work perfectly due to the hardware's quality.

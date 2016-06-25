sarrus_cramer
======
##[Using Rule of Sarrus, Cramer's Rule, and Python to Solve a System of Three Linear Equations](http://mikequentelsoftware.blogspot.ca/2012/06/using-rule-of-sarrus-cramers-rule-and.html)
```
# System of three linear equations
# ax + by + cz = j
# dx + ey + fz = k
# gx + hy + iz = l

# System of three linear equations in matrix notation
#  -         -   - -       - -
# | a   b   c | | x |     | j |
# |           | |   |     |   |
# | d   e   f | | y |  =  | k |
# |           | |   |     |   |
# | g   h   i | | z |     | l |
#  -         -   - -       - -

# Matrix of Coefficients
# a b c
# d e f
# g h i

# Matrix of Variables
# x
# y
# z

# Matrix of Resulting Values
# j
# k
# l

# Rule of Sarrus
# a b c|a b
# d e f|d e
# g h i|g h

# Rule of Sarrus Index Values
# 0 1 2|0 1
# 3 4 5|3 4
# 6 7 8|6 7

# Determinant
# det(M) = aei + bfg + cdh - gec - hfa - idb

# Cramer's Rule
# | j b c |   | a j c |   | a b j |
# | k e f |   | d k f |   | d e k |
# | l h i |   | g l i |   | g h l |
# ---------,  ---------,  ---------
# | a b c |   | a b c |   | a b c |
# | d e f |   | d e f |   | d e f | 
# | g h i |   | g h i |   | g h i |
```

#!/usr/bin/python

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
import sys

def main():

  inputs_dict = {'a':int(raw_input("a:")), 'b':int(raw_input("b:")), 'c':int(raw_input("c:")), 'j':int(raw_input("j:")),
  'd':int(raw_input("d:")), 'e':int(raw_input("e:")), 'f':int(raw_input("f:")), 'k':int(raw_input("k:")),
  'g':int(raw_input("g:")), 'h':int(raw_input("h:")), 'i':int(raw_input("i:")), 'l':int(raw_input("l:"))}

  coeffs_matrix = {'a':inputs_dict['a'], 'b':inputs_dict['b'], 'c':inputs_dict['c'],
  'd':inputs_dict['d'], 'e':inputs_dict['e'], 'f':inputs_dict['f'],
  'g':inputs_dict['g'], 'h':inputs_dict['h'], 'i':inputs_dict['i']}
  x_numerator_matrix = {'j':inputs_dict['j'], 'b':inputs_dict['b'], 'c':inputs_dict['c'],
  'k':inputs_dict['k'], 'e':inputs_dict['e'], 'f':inputs_dict['f'],
  'l':inputs_dict['l'], 'h':inputs_dict['h'], 'i':inputs_dict['i']}
  y_numerator_matrix = {'a':inputs_dict['a'], 'j':inputs_dict['j'], 'c':inputs_dict['c'],
  'd':inputs_dict['d'], 'k':inputs_dict['k'], 'f':inputs_dict['f'],
  'g':inputs_dict['g'], 'l':inputs_dict['l'], 'i':inputs_dict['i']}
  z_numerator_matrix = {'a':inputs_dict['a'], 'b':inputs_dict['b'], 'j':inputs_dict['j'],
  'd':inputs_dict['d'], 'e':inputs_dict['e'], 'k':inputs_dict['k'],
  'g':inputs_dict['g'], 'h':inputs_dict['h'], 'l':inputs_dict['l']}

  # Rule of Sarrus for det_coeffs_matrix
  # a b c|a b
  # d e f|d e
  # g h i|g h
  #
  det_coeffs_matrix = (coeffs_matrix['a'] * coeffs_matrix['e'] * coeffs_matrix['i'] +
  coeffs_matrix['b'] * coeffs_matrix['f'] * coeffs_matrix['g'] +
  coeffs_matrix['c'] * coeffs_matrix['d'] * coeffs_matrix['h'] -
  coeffs_matrix['g'] * coeffs_matrix['e'] * coeffs_matrix['c'] -
  coeffs_matrix['h'] * coeffs_matrix['f'] * coeffs_matrix['a'] -
  coeffs_matrix['i'] * coeffs_matrix['d'] * coeffs_matrix['b'])

  # Rule of Sarrus for det_x_numerator_matrix
  # j b c|j b
  # k e f|k e
  # l h i|l h
  #
  det_x_numerator_matrix = (x_numerator_matrix['j'] * x_numerator_matrix['e'] * x_numerator_matrix['i'] +
  x_numerator_matrix['b'] * x_numerator_matrix['f'] * x_numerator_matrix['l'] +
  x_numerator_matrix['c'] * x_numerator_matrix['k'] * x_numerator_matrix['h'] -
  x_numerator_matrix['l'] * x_numerator_matrix['e'] * x_numerator_matrix['c'] -
  x_numerator_matrix['h'] * x_numerator_matrix['f'] * x_numerator_matrix['j'] -
  x_numerator_matrix['i'] * x_numerator_matrix['k'] * x_numerator_matrix['b'] )

  # Rule of Sarrus for det_y_numerator_matrix
  # a j c|a j
  # d k f|d k
  # g l i|g l
  #
  det_y_numerator_matrix = (y_numerator_matrix['a'] * y_numerator_matrix['k'] * y_numerator_matrix['i'] +
  y_numerator_matrix['j'] * y_numerator_matrix['f'] * y_numerator_matrix['g'] +
  y_numerator_matrix['c'] * y_numerator_matrix['d'] * y_numerator_matrix['l'] -
  y_numerator_matrix['g'] * y_numerator_matrix['k'] * y_numerator_matrix['c'] -
  y_numerator_matrix['l'] * y_numerator_matrix['f'] * y_numerator_matrix['a'] -
  y_numerator_matrix['i'] * y_numerator_matrix['d'] * y_numerator_matrix['j'])

  # Rule of Sarrus for det_z_numerator_matrix
  # a b j|a b
  # d e k|d e
  # g h l|g h
  #
  det_z_numerator_matrix = (z_numerator_matrix['a'] * z_numerator_matrix['e'] * z_numerator_matrix['l'] +
  z_numerator_matrix['b'] * z_numerator_matrix['k'] * z_numerator_matrix['g'] +
  z_numerator_matrix['j'] * z_numerator_matrix['d'] * z_numerator_matrix['h'] -
  z_numerator_matrix['g'] * z_numerator_matrix['e'] * z_numerator_matrix['j'] -
  z_numerator_matrix['h'] * z_numerator_matrix['k'] * z_numerator_matrix['a'] -
  z_numerator_matrix['l'] * z_numerator_matrix['d'] * z_numerator_matrix['b'])

  x = det_x_numerator_matrix/det_coeffs_matrix
  y = det_y_numerator_matrix/det_coeffs_matrix
  z = det_z_numerator_matrix/det_coeffs_matrix

  print
  print "results: "
  print "x = " + str(x)
  print "y = " + str(y)
  print "z = " + str(z)

# Specifies name of main function.
if __name__ == "__main__":
  sys.exit(main())

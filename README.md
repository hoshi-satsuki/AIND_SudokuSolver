# Sudoku Solver

## Introduction
This project serves as a sudoku solver. The sudoku
solver follows the standard rules for a 9x9 sudoku with the
additional rule that the numbers 0 to 9 must only appear once
on each diagonal.  
This project has been part of the Artificial Intelligence Nanodegree on Udacity.

## The strategy
The solver searches through the possible assignments using constraint propagation and backtracking.  
For constraint propagation the following rules are implemented:  
### Elimination:
If a value has shown up once within a unit (that
is a 3x3 square, a row, a column or a diagonal), we eliminate
it from the list of possible values of all the other boxes in
the unit.  
### Only Choice:
If a value shows up only once in the lists of
possible value of the boxes within one unit, that value is
assigned to that box.
### Naked Twins:
If two values appear as a pair in two boxes within one unit
these values are eliminated from the other boxes.

## Usage
Execute solution.py and an example sudoku will be solved. For the visualizations to work pygame is needed.

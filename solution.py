rows = 'ABCDEFGHI'
cols = '123456789'

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s+t for s in A for t in B]





assignments = []

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
        
    """

    boxes=values.keys()
    
    row_unitlist = [cross(r, cols) for r in rows]
    row_units = dict((s, [u for u in row_unitlist if s in u]) for s in boxes)
    row_peers = dict((s, set(sum(row_units[s],[]))-set([s])) for s in boxes)
    
    column_unitlist = [cross(rows, c) for c in cols]
    col_units = dict((s, [u for u in column_unitlist if s in u]) for s in boxes)
    col_peers = dict((s, set(sum(col_units[s],[]))-set([s])) for s in boxes)
    
    square_unitlist = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
    sq_units = dict((s, [u for u in square_unitlist if s in u]) for s in boxes)
    sq_peers = dict((s, set(sum(sq_units[s],[]))-set([s])) for s in boxes)
    
    diag_unit1list=[[rows[i]+cols[i] for i in range(len(rows))]]
    diag_units1 = dict((s, [u for u in diag_unit1list if s in u]) for s in boxes)
    diag1_peers = dict((s, set(sum(diag_units1[s],[]))-set([s])) for s in boxes)
    
    diag_unit2list=[[rows[i]+cols[len(cols)-i-1] for i in range(len(rows))]]        
    diag_units2 = dict((s, [u for u in diag_unit2list if s in u]) for s in boxes)
    diag2_peers = dict((s, set(sum(diag_units2[s],[]))-set([s])) for s in boxes)
    
    

    for box in values.keys():
        if len(values[box])==2:
            for box2 in row_peers[box]:
                if values[box2]==values[box]:
                    digit1=values[box2][0]
                    digit2=values[box2][1]
                    for box3 in row_peers[box]:
                        if box3!=box2:
                            values=assign_value(values,box3,values[box3].replace(digit1,''))
                            values=assign_value(values,box3,values[box3].replace(digit2,''))
            for box2 in col_peers[box]:
                if values[box2]==values[box]:
                    digit1=values[box2][0]
                    digit2=values[box2][1]
                    for box3 in col_peers[box]:
                        if box3!=box2:
                            values=assign_value(values,box3,values[box3].replace(digit1,''))
                            values=assign_value(values,box3,values[box3].replace(digit2,''))
            for box2 in sq_peers[box]:
                if values[box2]==values[box]:
                    digit1=values[box2][0]
                    digit2=values[box2][1]
                    for box3 in sq_peers[box]:
                        if box3!=box2:
                            values=assign_value(values,box3,values[box3].replace(digit1,''))
                            values=assign_value(values,box3,values[box3].replace(digit2,''))
            for box2 in diag1_peers[box]:
                if values[box2]==values[box]:
                    digit1=values[box2][0]
                    digit2=values[box2][1]
                    for box3 in diag1_peers[box]:
                        if box3!=box2:
                            values=assign_value(values,box3,values[box3].replace(digit1,''))
                            values=assign_value(values,box3,values[box3].replace(digit2,''))
            for box2 in diag2_peers[box]:
                if values[box2]==values[box]:
                    digit1=values[box2][0]
                    digit2=values[box2][1]
                    for box3 in diag2_peers[box]:
                        if box3!=box2:
                            values=assign_value(values,box3,values[box3].replace(digit1,''))
                            values=assign_value(values,box3,values[box3].replace(digit2,''))   
    return values
   


 

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    
    boxes = cross(rows, cols)
    value = []
    all_digits = '123456789'
    for c in grid:
        if c == '.':
            value.append(all_digits)
        elif c in all_digits:
            value.append(c)
    assert len(value) == 81
    values=dict(zip(boxes,value))          
    for k in values.keys():
          values=assign_value(values, k, values[k])        
    return values
    


def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    boxes = values.keys()
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(values):
    """Eliminate values that are already there in the same unit.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the elements eliminated from peers.
        
    """
    row_units = [cross(r, cols) for r in rows]
    column_units = [cross(rows, c) for c in cols]
    square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
    diag_unit1=[[rows[i]+cols[i] for i in range(len(rows))]]
    diag_unit2=[[rows[i]+cols[len(cols)-i-1] for i in range(len(rows))]]
    unitlist = row_units + column_units + square_units + diag_unit1 + diag_unit2
    boxes=values.keys()
    units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
    peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
    
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values=assign_value(values,peer,values[peer].replace(digit,''))
    return values

def only_choice(values):
    """Eliminate values using only choice strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the appropriate elements eliminated.
        
    """
    row_units = [cross(r, cols) for r in rows]
    column_units = [cross(rows, c) for c in cols]
    square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
    diag_unit1=[[rows[i]+cols[i] for i in range(len(rows))]]
    diag_unit2=[[rows[i]+cols[len(cols)-i-1] for i in range(len(rows))]]
    unitlist = row_units + column_units + square_units + diag_unit1 + diag_unit2
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values=assign_value(values,dplaces[0],digit)       
    return values

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        # Use the Eliminate Strategy
        values = eliminate(values)
        # Use the Only Choice Strategy
        values = only_choice(values)
        # Use the NakedTwins Strategy
        values= naked_twins(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    boxes=values.keys()
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and 
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt
    

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """

    values=grid_values(grid)
    solution=search(values)
    return solution




if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')

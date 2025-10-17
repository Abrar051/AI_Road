# Find the path from (0,0) > (3,3)
grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 0, 0, 0]
]

start = (0, 0)
move = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # right, down, up, left
end = (len(grid) - 1, len(grid[0]) - 1)


def position_Judge(coordinate):
    x_coordinate, y_coordinate = coordinate
    if grid[x_coordinate][y_coordinate] == 1:
        return False
    return True


def movement_List(coordinate, grid):
    moveList = []
    rows = len(grid)
    cols = len(grid[0])
    for dx, dy in move:
        x = coordinate[0] + dx
        y = coordinate[1] + dy
        if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0:
            newMove = (x, y)
            if position_Judge(newMove):
                moveList.append(newMove)
    return moveList


def path_finder(grid, start, end):
    path = [start]
    visited = set([start])
    current = start

    while current != end:
        possibleMoves = movement_List(current, grid)

        # Filter out already visited cells
        possibleMoves = [m for m in possibleMoves if m not in visited]

        if not possibleMoves:
            # Dead end, backtrack
            path.pop()
            if not path:
                print("No path found.")
                return []
            current = path[-1]
            continue

        # Move to the first unvisited cell
        nextMove = possibleMoves[0]
        visited.add(nextMove)
        path.append(nextMove)
        current = nextMove

        # Safety break (avoid infinite loop)
        if len(path) > len(grid) * len(grid[0]):
            print("Loop detected. Breaking.")
            break

    return path


print("Path finder:", path_finder(grid, start, end))

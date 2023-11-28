def ChinaandJapanSea(strArr):
    def parse_input(str_list):
        return [list(map(int, row.strip("[]").split(","))) for row in str_list]

    # first, parse the input
    heights = parse_input(strArr)

    # Exceptional input handling
    if not heights or not heights[0]:
        return []

    # setup 2D array that each coordinate indicates whether the coordinate can flow to each sea
    num_rows, num_cols = len(heights), len(heights[0])
    china_reachable = [[False for _ in range(num_cols)] for _ in range(num_rows)]
    east_reachable = [[False for _ in range(num_cols)] for _ in range(num_rows)]

    # using DFS; Depth-First Search
    def dfs(row, col, reachable):
        # Base condition
        if reachable[row][col]:
            return
        reachable[row][col] = True

        # each tuple means: up(-y), down(+y), left(-x), right(+x)
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dy, col + dx
            if (0 <= new_row < num_rows and
                    0 <= new_col < num_cols and
                    heights[new_row][new_col] >= heights[row][col]):
                dfs(new_row, new_col, reachable)

    # Start DFS from all cells adjacent to the oceans
    for x in range(num_cols):
        dfs(0, x, china_reachable)
        dfs(num_rows - 1, x, east_reachable)
    for y in range(num_rows):
        dfs(y, 0, china_reachable)
        dfs(y, num_cols - 1, east_reachable)

    # result means the intersection of cells reachable to both oceans
    result = [[y, x] for y in range(num_rows) for x in range(num_cols)
              if china_reachable[y][x] and east_reachable[y][x]]

    # it was hard though
    # and this can be done in time complexity of O(n*m) as I did above
    return result


# test cases!
print(ChinaandJapanSea(["[1,2,2,3,5]", "[3,2,3,4,4]", "[2,4,5,3,1]", "[6,7,1,4,5]", "[5,1,1,2,4]"]))
print(ChinaandJapanSea(["[2,1]", "[1,2]"]))
print(ChinaandJapanSea(["[1,2,3,4,5]"]))
print(ChinaandJapanSea(["[1]", "[2]", "[3]", "[4]", "[5]"]))
print(ChinaandJapanSea(["[2,2,2]", "[2,2,2]", "[2,2,2]"]))
print(ChinaandJapanSea(["[1,2,3]", "[2,3,4]", "[3,4,5]"]))
print(ChinaandJapanSea(["[5,4,3]", "[4,3,2]", "[3,2,1]"]))

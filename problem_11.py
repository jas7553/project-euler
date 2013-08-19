'''Jason A Smith'''
grid = [[int(i) for i in line.split()] for line in open('problem_11.txt')]
biggest = 0

for row in range(len(grid)):
    for col in range(len(grid[row])):
        rowProduct = 1
        colProduct = 1
        lrDiagProduct = 1
        rlDiagProduct = 1

        for step in range(4):
            if col + step < len(grid[row]):
                rowProduct *= grid[row][col + step]

            if row + step < len(grid):
                colProduct *= grid[row + step][col]
            
            if col + step < len(grid[row]) and row + step < len(grid):
                lrDiagProduct *= grid[row + step][col + step]

            if col - step > 0 and row + step < len(grid):
                rlDiagProduct *= grid[row + step][col - step]

        biggest = max(biggest, rowProduct, colProduct, lrDiagProduct, rlDiagProduct)

print(biggest)

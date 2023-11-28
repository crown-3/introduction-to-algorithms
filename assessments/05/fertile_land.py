import ast


def FertileLand2(strArr):
    # ah, welcome to the rice field, ***
    land, k = ast.literal_eval(strArr[0]), int(strArr[1])

    # initialize the histogram (based on threshold k)
    hist = [0 if x < k else 1 for x in land[0]]
    max_area = largest_rectangle_area(hist)

    # build the histogram, iterating through rows of the field
    for i in range(1, len(land)):
        for j in range(len(land[i])):
            # reset the histogram if yield < threshold
            if land[i][j] < k:
                hist[j] = 0
            else:
                # if the land is fertile -> add it to the histogram
                hist[j] += 1
        # find the largest rectangle in the histogram
        max_area = max(max_area, largest_rectangle_area(hist))

    return max_area


# this function will get the largest rectangle area (in the histogram)
def largest_rectangle_area(heights):
    stack = [-1]
    max_area = 0
    for i in range(len(heights)):
        # pop the stack; until the current height is greater than the top of the stack
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            last = stack.pop()
            max_area = max(max_area, heights[last] * (i - stack[-1] - 1))
        stack.append(i)

    # calculate the area for the remaining elements
    while stack[-1] != -1:
        last = stack.pop()
        max_area = max(max_area, heights[last] * (len(heights) - stack[-1] - 1))

    return max_area


# Example input
example_input = ["[[1,10,20,3],[9,8,7,6],[20,30,20,11],[9,6,3,5]]", "6"]
# Calling the function with the example input
FertileLand2(example_input)

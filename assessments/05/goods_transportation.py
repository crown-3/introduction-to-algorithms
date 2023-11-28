import ast
from heapq import nsmallest


def euclidean_distance(a, b):
    # 'cause we need only relative comparison, we do not apply sqrt
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def Goodtransportation2(strArr):
    # let's parse the input
    x = ast.literal_eval(strArr[0])
    y = ast.literal_eval(strArr[1])
    warehouse = ast.literal_eval(strArr[2])
    k = int(strArr[3])

    # zip the x and y coordinates together
    points = list(zip(x, y))
    distances = [(euclidean_distance(point, warehouse), point) for point in points]

    # extract k closest points from distances
    k_closest = nsmallest(k, distances)
    result = [str(point[1]) for point in k_closest]

    return result


# Test the function with the example input
print(Goodtransportation2(["[-1, 0, -2, 2, -3]", "[0, 2, -1, -2, -3]", "[-2, 0]", "2"]))
print(Goodtransportation2(["[-1, 0, -2, 2, -3]", "[0, 2, -1, -2, -3]", "[-2, 0]", "3"]))
print(Goodtransportation2(["[-2, -2, -2]", "[0, 0, 0]", "[-2, 0]", "2"]))  # all points' location is same as warehouse's
print(Goodtransportation2(["[-1, 0, -2]", "[0, 2, -1]", "[-2, 0]", "5"]))  # k is larger than available points
print(Goodtransportation2(["[-2, -1, 1, 2]", "[1, -1, 2, -2]", "[0, 0]", "3"]))  # equidistant
print(Goodtransportation2(["[]", "[]", "[0, 0]", "2"]))  # no demand points

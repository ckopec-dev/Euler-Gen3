# Project Euler Problem 91: Right triangles with integer coordinates

def count_right_triangles(grid_size):
    count = 0

    # Iterate through all possible points (x1, y1) and (x2, y2)
    for x1 in range(grid_size + 1):
        for y1 in range(grid_size + 1):
            for x2 in range(grid_size + 1):
                for y2 in range(grid_size + 1):
                    # Skip the origin point (0, 0) and identical points
                    if (x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0) or (x1 == x2 and y1 == y2):
                        continue

                    # Check if the points form a right triangle
                    # Calculate the squared lengths of the sides
                    side1 = x1**2 + y1**2
                    side2 = x2**2 + y2**2
                    side3 = (x2 - x1)**2 + (y2 - y1)**2

                    # Check if the triangle satisfies the Pythagorean theorem
                    sides = sorted([side1, side2, side3])
                    if sides[0] + sides[1] == sides[2]:
                        count += 1

    # Each triangle is counted twice, so divide by 2
    return count // 2

if __name__ == "__main__":
    grid_size = 50  # Change this value for different grid sizes
    result = count_right_triangles(grid_size)
    print(f"Number of right triangles in a {grid_size}x{grid_size} grid: {result}")
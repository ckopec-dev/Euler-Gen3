# Problem 102: Triangle Containment
# A program to determine how many triangles contain the origin in their interior.

# Function to calculate the area of a triangle given its vertices
def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2

# Function to check if the origin is inside the triangle
def contains_origin(x1, y1, x2, y2, x3, y3):
    total_area = triangle_area(x1, y1, x2, y2, x3, y3)
    area1 = triangle_area(0, 0, x2, y2, x3, y3)
    area2 = triangle_area(x1, y1, 0, 0, x3, y3)
    area3 = triangle_area(x1, y1, x2, y2, 0, 0)
    return total_area == area1 + area2 + area3

# Read the triangle data from the file
with open("triangles.txt", "r") as file:
    triangles = [list(map(int, line.strip().split(','))) for line in file]

# Count triangles containing the origin
count = 0
for triangle in triangles:
    if contains_origin(*triangle):
        count += 1

print("Number of triangles containing the origin:", count)
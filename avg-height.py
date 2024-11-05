# write a list of student heights
print("Enter the heights of people in cm, separated by a space: ")
people_heights = input().split()
for n in range(0, len(people_heights)):
    people_heights[n] = int(people_heights[n])

# people heights start from 0th index, so we add 1
people = n + 1
total_height = 0
for height in people_heights:
    total_height += height
    avg_height = round(total_height / people)
print(f"total height = {total_height}")
print(f"number of students = {people}")
print(f"average height = {avg_height}")
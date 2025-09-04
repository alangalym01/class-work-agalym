from shapes import Rectangle, Circle, Triangle
from utils import *

# ask user for their shape choice
choice = int(input("Which shape would you like to create? 1 - Rectangle, 2 - Circle, 3 - Triangle: "))

# keep asking until they enter a valid choice
while choice < 1 or choice > 3:
    print("Invalid choice.")
    choice = int(input("Which shape would you like to create? 1 - Rectangle, 2 - Circle, 3 - Triangle: "))

# calculate the area and generate a description of the chosen shape
if choice == 1:
    rect_height = int(input("Enter rectangle height: "))
    rect_width = int(input("Enter rectangle width: "))

    rect = Rectangle(rect_height, rect_width)
    rect.describe()

elif choice == 2:
    circle_radius = int(input("Enter the radius of the circle: "))

    circle = Circle(circle_radius)
    circle.describe()

elif choice == 3:
    triangle_height = int(input("Enter triangle height: "))
    triangle_base = int(input("Enter triangle base length: "))

    triangle = Triangle(triangle_height, triangle_base)
    triangle.describe()

# ask the user if they would like to convert the area from cm^2 to m^2
convert_to_cm_sq = input("Would you like to convert cm^2 to m^2? ")
if convert_to_cm_sq == "yes":
    if choice == 1:
            converted_value = cm_squared_to_m_squared(rect.area())
    elif choice == 2:
        converted_value = cm_squared_to_m_squared(circle.area())
    elif choice == 3:
        converted_value = cm_squared_to_m_squared(triangle.area())
    print(f"Your converted value is {converted_value} m^2")

    # give the user an option to convert the area back to cm^2
    convert_to_m_sq = input("Would you like to convert m^2 back to cm^2? ")
    if convert_to_m_sq == "yes":
        if choice == 1:
                converted_value = m_squared_to_cm_squared(rect.area())
        elif choice == 2:
            converted_value = m_squared_to_cm_squared(circle.area())
        elif choice == 3:
            converted_value = m_squared_to_cm_squared(triangle.area())
        print(f"Your converted value is {converted_value} cm^2")
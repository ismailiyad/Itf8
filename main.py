def check_area(area):
    print(f"Area is {area}")

    if area >= 10:
        print("area is bigger than 10")
    elif area >= 0:
        print("area is maller than 10")
    else:
        print("invalid area")




def triangle_area(base,height):
    area = 0.5 * base * height
    check_area(area)

def circle_area(radius):
    area = 3.14 * (radius ** 2)
    check_area(area)

def rectangle_area(length,width):
    area = length * width
    check_area(area)


triangle_area(20,2)
circle_area(15)
rectangle_area(5,7)




building_type = ""
while building_type != "0":
    while True:
        building_type = input("What building type (residential (r) or "
                              "commercial (c)) exit (X): ")
        if building_type == "residential" or building_type == "r":
            building_type = 0.25
            break
        elif building_type == "commercial" or building_type == "c":
            building_type = 0.5
            break
        elif building_type == "X" or "x":
            print("Program ended Goodbye")
            building_type = "0"
            break
        else:
            print("Please enter a valid answer (r or c)")
    if building_type == "0":
        building_type = "0"
        break
    else:
        length = float(input("What length is the building?: "))
        width = float(input("What width is the building?: "))
        volume = float(length * width * building_type)
        print(f"The volume of concrete required for a slab with a\n"
              f"length of {length}m\na width of {width}m\nand a depth of "
              f"{building_type}m \nis {volume} cubic metres")

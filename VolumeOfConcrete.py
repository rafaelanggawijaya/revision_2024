building_type = ""
while building_type != "X" or building_type != "x": 
    while True:
            building_type = input("What building type (residential (r) or commercial (c)) exit (X): ")
            if building_type == "residential" or building_type == "r":
                building_type == float(0.25)
                break
            elif building_type == "commercial" or building_type == "c":
                building_type == float(0.5)
                break
            else:
                input("Please enter a valid answer (r or c)")

    length = float(input("What length is the building?: "))
    width = float(input("What width is the building?: "))
    volume = length*width*building_type
    print(f"The volume of concrete required for a slab with a\nlength of {length}m\na width of {width}m\nand a depth of {building_type}m is {volume} cubic metres")
    
            

    

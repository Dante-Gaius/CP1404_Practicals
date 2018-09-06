COLOR_NAMES = {"ALICE BLUE": "#f0f8ff", "ANTIQUE WHITE": "#faebd7", "BEIGE": "#f5f5dc", "BLACK": "#000000",
               "BLANCHED ALMOND": "#ffebcd", "BLUE VIOLET": "#8a2be2", "BROWN": "a52a2a", "BURLY WOOD": "#deb887",
               "CADET BLUE": "5f9ea0", "CHOCOLATE": "#d2691e"}

for colors in COLOR_NAMES:
    print("{:15} is {}".format(colors, COLOR_NAMES[colors]))

color = input("Enter color name: ")
color = color.upper()
while color != "":
    if color in COLOR_NAMES:
        print(color, "is", COLOR_NAMES[color])
    else:
        print("Invalid color name")
    color = input("Enter color name: ")
    color = color.upper()

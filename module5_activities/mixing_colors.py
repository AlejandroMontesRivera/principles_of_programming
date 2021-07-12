# When you mix red and blue, you get purple. /  When you mix red and yellow, you get orange. / When you mix blue and
# yellow, you get green. Design a program that prompts the user to enter the names of two primary colors to mix. If
# the user enters anything other than "red," "blue," or "yellow," the program should display an error message.
# Otherwise, the program should display the name of the secondary color that results.

color_pri = input('Introduce the first RGB color you want to mix: ').lower()
color_sec = input('Introduce the second RGB color you want to mix: ').lower()


def color_init(color_base, val):
    return val if color_pri == color_base or color_sec == color_base else 0


# Designed a way to input the response in RGB
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


# Validate color input function
def val_color(color_base):
    return color_base == 'red' or color_base == 'yellow' or color_base == 'blue'


# Validate input
if val_color(color_pri) and val_color(color_sec):

    # Init RGB
    red = 0
    green = 0
    blue = 0

    # Determine if red was introduced
    red += color_init("red", 255)
    # Determine if yellow was introduced
    red += color_init("yellow", 255)
    green += color_init("yellow", 255)
    # Determine if blue was introduced
    blue += color_init("blue", 255)

    if red > 255 or green > 255 or blue > 255:
        red = int(red / 2)
        green = int(green / 2)
        blue = int(blue / 2)
    if red == 255 and green == 0 and blue == 0:  # red - red
        color = 'Red'
    if red == 255 and green == 255 and blue == 0:  # yellow - yellow
        color = 'Yellow'
    if red == 0 and green == 0 and blue == 255:  # blue - blue
        color = 'Blue'
    if red == 255 and green == 0 and blue == 255:  # red - blue
        color = 'Purple'
    if red == 255 and green == 127 and blue == 0:  # red - yellow
        color = 'Orange'
    if red == 255 and green == 255 and blue == 255:  # yellow - blue
        color = 'Green'  # INTERESTING: In RGB Blue and Yellow make White, because of the light spectrum
        red = 0
        blue = 0

    print(f"red: {red}, green: {green}, blue: {blue}")
    print(f"{colored(red, green, blue, color)}")
else:
    print("ERROR, ENTER A VALID PRIMARY COLOR")

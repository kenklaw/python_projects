import turtle

handle = open('stars.txt', 'r')

# Reads file and groups catagories of important values

def read_file(filehandle):
    data = filehandle.readlines()
    coordinates = {}
    hd_mag = {}
    namesdict = {}
    for elem in data:
        caterogry = elem.split(" ", 6)
        x = caterogry[0]
        y = caterogry[1]
        hd = caterogry[3]
        mag = caterogry[4]
        hrvd = caterogry[5]
        if len(caterogry) > 6:
            names = caterogry[6]
            names = names.strip("\n")
            namesdict[names] = hd
        hd_mag[hd] = mag
        coordinates[hd] = (x, y)
    return coordinates, namesdict, hd_mag

coordinates, namesdict, hd_mag = read_file(handle)

# speed of program
#turtle.tracer(0)
turtle.speed(500)
# Draws stars and impliments Magnitude setting

def plot_by_magnitude(picture_size, coordinates, hd_mag):

    turtle.setup(picture_size, picture_size)
    turtle.bgcolor("black")
    turtle.pencolor("white")

    for i in coordinates:
        star_size = round(10.0/(float(hd_mag[i])+2))
        if star_size >= 8:
            star_size = 8
        plot_scale = (picture_size / 2)
        star_coords = coordinates[i]
        star_x = float(star_coords[0])
        star_y = float(star_coords[1])
        turtle.home()
        turtle.pu()
        turtle.goto(star_x * plot_scale, star_y * plot_scale)
        turtle.begin_fill()
        turtle.color("white")
        turtle.pd()
        for i in range(4):
            turtle.forward(star_size)
            turtle.right(90)
        turtle.end_fill()
        turtle.pu()

plot_by_magnitude(850, coordinates, hd_mag)

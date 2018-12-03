import color
import gray
import map
import rgb
import var
def colorSave(file):
    color.color(file, 1)
    color.color(file, 2)
    color.color(file, 3)
    gray.gray(file)
    map.map(file)
    rgb.rgb(file)
    var.var(file)
#colorSave("fruit")
import combine
import colorSave
import texture
def feature(file, a = 0):
    if a == 0:
        colorSave.colorSave(file)
        texture.texture(file)
    if a == 1:
        combine.combine(file)
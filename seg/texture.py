import db1
import haar
import inverse
def texture(file):
    db1.w2d(file)
    haar.w2d(file)
    inverse.inverse(file)
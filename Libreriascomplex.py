import math

def sumacplx(c1,c2):
    sumaR = c1[0] + c2[0]
    sumaI = c1[1] + c2[1]
    return (sumaR, sumaI)

def producto(c1,c2):
    prodR = (c1[0] * c2[0]) - (c1[1] * c2[1])
    prodI = (c1[0] * c2[1]) + (c2[0] * c1[1])
    return (prodR, prodI)

def resta(c1, c2):
    restaR = c1[0] - c2[0]
    restaI = c1[1] - c2[1]
    return (restaR, restaI)

def division(c1,c2):
    num1 = (c1[0] * c2[0]) + (c1[1] * c2[1])
    num2 = -1*((c1[0] * c2[1]) - (c2[0] * c1[1]))
    dem = c2[0]**2 + c2[1]**2
    return(num1/dem, num2/dem)

def modulo(c1):
    mod = ((c1[0] ** 2) + (c1[1] ** 2)) ** 0.5
    return mod

def conjugado(c1):
    conju = (c1[0], -1 * c1[1])
    return (conju)

def carteapolar(c1):
    p = ((c1[0] ** 2) + (c1[1] ** 2)) ** 0.5
    angulo = math.atan(c1[1] / c1[0])
    return (p,angulo)

def polaracarte(c1):
    a = (((c1[0] ** 2) + (c1[1] ** 2)) ** 0.5)*math.cos(math.atan(c1[1] / c1[0]))
    b = (((c1[0] ** 2) + (c1[1] ** 2)) ** 0.5)*math.sin(math.atan(c1[1] / c1[0]))
    return (a,b)

def fase(c1):
    b = math.atan(c1[1] / c1[0])
    return (b)
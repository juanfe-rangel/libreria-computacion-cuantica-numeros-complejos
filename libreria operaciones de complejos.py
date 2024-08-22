import math 
def suma(a,b):
    real = a[0]+b[0]
    complejo =a[1]+b[1]
    return (real,complejo)

def resta(a,b):
    real = a[0]-b[0]
    complejo = a[1]-b[1]
    return(real,complejo)

def producto(a,b):
    real = (a[0]*b[0])-(a[1]*b[1])
    complejo = (a[0]*b[1])+(a[1]*b[0])
    return (real,complejo)

def division(a,b):
    real = ((a[0]*b[0])+(a[1]*b[1]))/((b[0]**2)+(b[1]**2))
    complejo = ((b[0]*a[1])-(a[0]*b[1]))/((b[0]**2)+(b[1])**2)
    return (real,complejo)

def conjugado(a):
    return(a[0],-a[1])

def modulo(a):
    modulo=math.sqrt(a[0]*a[0]+a[1]*a[1])
    return modulo

def polar(a):
    r = modulo(a)
    f = math.atan(a[1]/a[0])
    return (r,f)

def rectangular(a):
    real = a[0]*math.cos(a[1])
    complejo = a[0]*math.sin(a[1])
    return(real,complejo)

def fase(a):
    return math.atan(a[1]/a[0])


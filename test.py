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

a=suma((2,2),(2,3))
print(a)
b=suma((3,5),(5,7))
print(b)
a=resta((2,2),(2,3))
print(a)
b=resta((3,5),(5,7))
print(b)
a=producto((2,2),(2,3))
print(a)
b=producto((3,5),(5,7))
print(b)
a=division((2,2),(2,3))
print(a)
b=division((3,5),(5,7))
print(b)
a=conjugado((2,3))
print(a)
b=conjugado((5,7))
print(b)
a=modulo((2,3))
print(a)
b=modulo((5,7))
print(b)
a=polar((2,3))
print(a)
b=polar((5,7))
print(b)
a=rectangular((2,3))
print(a)
b=rectangular((5,7))
print(b)
a=fase((2,3))
print(a)
b=fase((5,7))
print(b)
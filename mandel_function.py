def mandelbrot(c,iterations=100):
    z=0
    n=0
    
    
    
    while abs(z)<=2 and n< iterations:
        z=z**2+c
        n+=1
        
    return n



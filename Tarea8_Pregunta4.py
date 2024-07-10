def sumatoria(numero):
    if numero == 0:
        return 0
    else:
        return numero + sumatoria(numero - 1)
    
print (f"La sumatoria de 5 es: {sumatoria(5)}")
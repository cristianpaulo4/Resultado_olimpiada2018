

def calcular_piso(lag, comp):
    t2_lag = lag - 1
    t2_comp = comp - 1

    tipo2 = (t2_comp + t2_lag)*2
    tipo1 = (lag * comp) + ((t2_comp) * t2_lag)
    return tipo1,tipo2
    


    

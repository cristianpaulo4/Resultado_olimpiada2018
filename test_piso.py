from piso import calcular_piso

def test_piso_escola1():
    assert calcular_piso(3,5) == (23,12)

def test_piso_escola2():
    assert calcular_piso(1,1) == (1,0)

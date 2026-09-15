import numpy as np

def mult_matricial(A,B):
    a,b = A.shape
    c,d = B.shape

    if b != c:
        raise ValueError(
            "Las columnas de A no coinciden con las filas de B"
        )
    res = np.zeros((a,d))

    for i in range(a):
        for j in range(d):
            num = 0
            for k in range(b):
                num += A[i,k]*B[k,j]
            res[i,j] = num

    return res




def test_multiplicar_matrices():
    # Test 1: Multiplicación válida de matrices cuadradas (2x2 @ 2x2)
    A = np.array([[1.0, 2.0], [3.0, 4.0]])
    B = np.array([[2.0, 0.0], [1.0, 2.0]])
    resultado_esperado = np.array([[4.0, 4.0], [10.0, 8.0]])
    
    # Comprobamos con np.allclose para evitar problemas de precisión flotante
    assert np.allclose(mult_matricial(A, B), resultado_esperado), "Error en multiplicación 2x2"

    # Test 2: Multiplicación válida de matrices no cuadradas (2x3 @ 3x2 -> 2x2)
    C = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    D = np.array([[7.0, 8.0], [9.0, 1.0], [2.0, 3.0]])
    esperado_rect = np.array([[31.0, 19.0], [85.0, 55.0]])
    
    assert np.allclose(mult_matricial(C, D), esperado_rect), "Error en multiplicación (2x3 @ 3x2)"

    # Test 3: Propiedad del elemento neutro (Multiplicación por Matriz Identidad)
    I = np.eye(2)
    assert np.allclose(mult_matricial(A, I), A), "Error con matriz identidad"

    # Test 4: Captura de ValueError ante dimensiones incompatibles (2x3 @ 2x2)
    error_capturado = False
    E = np.ones((2, 3))
    F = np.ones((2, 2))
    
    try:
        mult_matricial(E, F)
    except ValueError:
        error_capturado = True  # El error fue lanzado correctamente
        
    assert error_capturado, "Se esperaba un ValueError por dimensiones incompatibles y no se lanzó"

    print("¡Todos los tests pasaron exitosamente!")

# Ejecutamos los tests
test_multiplicar_matrices()

def mult_vectorial(a,b):
    if a == [] or b == []:
        return 0
    elif len(a) != len(b):
        return 0
    res = 0
    for i in range(len(a)):
        res += a[i]*b[i]
    return res
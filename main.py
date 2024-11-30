def sumar(a, b):
    """Suma dos números."""
    return a + b

def restar(a, b):
    """Resta dos números."""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b

def dividir(a, b):
    """Divide dos números."""
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b


if __name__ == "__main__":
    
    print("Suma:", sumar(18, 21))
    print("Resta:", restar(34, 26))
    print("Multiplicación:", multiplicar(9, 3))
    print("División:", dividir(10, 5))

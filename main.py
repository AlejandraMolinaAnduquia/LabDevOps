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
    
    print("Suma:", sumar(3, 5))
    print("Resta:", restar(10, 4))
    print("Multiplicación:", multiplicar(6, 7))
    print("División:", dividir(8, 2))

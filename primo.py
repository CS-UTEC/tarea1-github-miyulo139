"""El algoritmo ha sido diseñado considerando que el
máximo divisor de un número 'n' compuesto no es mayor
a la mitad de n, y por ende es innecesario confirmar
si n es divisible o no con un número mayor que n//2.

* Se indicó si 2, 3 y 4 eran primos o no para evitar
los casos de rangos inválidos(2,1) y (2,2) si eran
evaluados en el iterador for. En caso se desee incluir
al 3 y 4, el rango debería de abarcar desde el 2
hasta n; sin embargo el costo de ejecución sería
mucho mayor en números elevados."""

def es_primo(num):
    if num < 2 or num == 4:
        return False
    elif num == 2 or num == 3:
        return True
    else:
        for i in range(2, num//2):
            if num % i == 0:
                return False
        return True

num= int(input('Ingrese número: '))

if es_primo(num):
  print(num, "es primo")
else:
  print(num, "no es primo")

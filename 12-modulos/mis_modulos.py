# File: Módulos hechos por mí.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

def holaMundo(nombre="Usuario"):
    return f"¡Hola! {nombre}, ten un buen día."


def porcentaje():
    num = (float(input("\nIngresa aqui el número al que le quieres sacar un porcentaje: ")))

    porciento = (float(input(f"\nIngresa aqúi el porcentaje que quieres saber de {num} : %")))
    porcentaje = (porciento*num / 100)

    # Redondear el decimal a centésimas o a dos cifras.
    print(f"\nEl {porciento}% de {num} es: {round(porcentaje,2)}")


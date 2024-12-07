import random
import string

def generar_contraseña(longitud, incluir_numeros=True, incluir_simbolos=True):
    caracteres = string.ascii_letters  # Letras mayúsculas y minúsculas
    if incluir_numeros:
        caracteres += string.digits  # Números
    if incluir_simbolos:
        caracteres += string.punctuation  # Símbolos (!, @, #, etc.)
    
    # Generar la contraseña aleatoria
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def main():
    print("¡Bienvenido al Generador de Contraseñas Yarbis!")
    while True:
        try:
            longitud = int(input("¿Cuántos caracteres quieres que tenga la contraseña? "))
            incluir_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
            incluir_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == 's'
            
            contraseña = generar_contraseña(longitud, incluir_numeros, incluir_simbolos)
            print(f"\nTu contraseña generada es:\n{contraseña}")
            
            # Preguntar si el usuario quiere generar otra contraseña
            otra_contraseña = input("\n¿Quieres generar otra contraseña? (s/n): ").lower()
            if otra_contraseña != 's':
                print("¡Gracias por usar el Generador de Contraseñas Yarbis!")
                break
        except ValueError:
            print("Por favor, ingresa un número válido para la longitud.")

if __name__ == "__main__":
    main()
# Así de sencillo es :)
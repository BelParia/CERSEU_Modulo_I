# Ejercicio 2
"""
Crea un programa que calcule el Índice de Masa Corporal
(IMC) de una persona.
La fórmula es: IMC = peso (kg)/altura (m^2)
En el mensaje también indicar el nombre de la persona indicando su
IMC también
"""
print("*** Calculadora de Índice de Masa Corporal ***\n")
nombre_usuario = "Brayan de la Cruz"
peso_usuario = 71
altura_usuario = 1.69
indice_masa_corporal = peso_usuario/pow(altura_usuario, 2)
categoria = ""
if indice_masa_corporal < 18.5:
    categoria = "Bajo"
elif 18.5 <= indice_masa_corporal <=25:
    categoria = "Normal"
elif 25 < indice_masa_corporal <= 30:
    categoria = "Sobrepeso"
    print("Cambia tu dieta, ejercitate a menudo. Tu puedes.")
else:
    categoria = "Obeso"
    print("Cambia tu dieta, ejercitate a menudo. Tu puedes.")
print(f"{nombre_usuario}, usted posee un IMC igual a {indice_masa_corporal:.1f},\n"
      f"asi que se encuentra en el grupo {categoria}")
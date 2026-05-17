# ============================================================
# Lógica de Programação — Python
# Disciplina: Lógica de Programação | ADS — CEUB | 2026
# Autor: José Orlando Vieira Xavier
# ============================================================


# ------------------------------------------------------------
# Exercício 1 — Contador com while
# Imprima os números de 1 a 10 usando while
# ------------------------------------------------------------

print("=== Exercício 1 — Contador ===")
contador = 0

while contador < 10:
    contador += 1
    print(contador)


# ------------------------------------------------------------
# Exercício 2 — Acumulador
# Calcule a soma dos números de 1 a 100
# ------------------------------------------------------------

print("\n=== Exercício 2 — Acumulador ===")
soma = 0
numero = 0

while numero < 100:
    numero += 1
    soma += numero

print(f"Soma de 1 a 100: {soma}")


# ------------------------------------------------------------
# Exercício 3 — Par ou Ímpar com módulo
# Verifique se os números de 1 a 20 são pares ou ímpares
# ------------------------------------------------------------

print("\n=== Exercício 3 — Par ou Ímpar ===")
numero = 0

while numero < 20:
    numero += 1

    if numero % 2 == 0:
        print(f"{numero} → Par")
    else:
        print(f"{numero} → Ímpar")


# ------------------------------------------------------------
# Exercício 4 — Tabuada com loops aninhados
# Gere a tabuada do 1 ao 5
# ------------------------------------------------------------

print("\n=== Exercício 4 — Tabuada ===")
tabuada = 0

while tabuada < 5:
    tabuada += 1
    multiplicador = 0

    print(f"\nTabuada do {tabuada}:")

    while multiplicador < 10:
        multiplicador += 1
        print(f"  {tabuada} x {multiplicador} = {tabuada * multiplicador}")


# ------------------------------------------------------------
# Exercício 5 — Média de notas
# Leia 5 notas e calcule a média, informando se foi aprovado
# ------------------------------------------------------------

print("\n=== Exercício 5 — Média de Notas ===")
notas = [7.5, 8.0, 6.5, 9.0, 7.0]  # notas fixas para simulação

soma = 0
contador = 0

for nota in notas:
    soma += nota
    contador += 1

media = soma / contador

print(f"Notas: {notas}")
print(f"Média: {media:.1f}")

if media >= 7.0:
    print("Resultado: APROVADO ✓")
elif media >= 5.0:
    print("Resultado: RECUPERAÇÃO")
else:
    print("Resultado: REPROVADO")

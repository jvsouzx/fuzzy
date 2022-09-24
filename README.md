### Funções e Operações Fuzzy

## 1 Implemente as funções de pertinência:
• Triangular: A(x; a, m, b) = max{min[(x − a)/(m − a), (b − x)/(b − m)], 0}
• Trapezoidal: A(x; a, m, n, b) = max{min[(x − a)/(m − a), 1, (b − x)/(b − m)], 0}
• Gaussiana: A(x) = e−k(x−m)2

## 2 Implemente os operadores de Complemento (C1 a C3), União (U1 a U4) e Interseção (I1
a I4):
• Zadeh: C1 = 1 − a
• Sugeno: C2 = 1−a
1+s.a , −1 < s < 0, s = 0, s > 0
• Yager: C3 = (1 − aw) 1
w , a < w < 0, w = 1, w > 1
• Máximo: U1 = max(a, b)
• Soma Probabilística: U2 = a + b − a.b
• Soma Limitada: U3 = min(1, a + b)
• Soma Drástica: U4 = a se b = 0, b se a = 0, 1 caso contrário.
• Mínimo: I1 = min(a, b)
• Produto: I2 = a.b
• Produto Limitado: I3 = max(0, a + b − 1)
• Produto Drástico: I4 = a se b = 1, b se a = 1, 0 caso contrário.

## 3 Apresente graficamente o resultado das implementações.
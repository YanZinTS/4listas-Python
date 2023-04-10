altura_j = 1.50  # altura inicial de Josberanilson em metros
altura_a = 1.10  # altura inicial de Apricoçildo em metros
taxa_cresc_j = 0.02  # taxa de crescimento de Josberanilson em metros por ano
taxa_cresc_a = 0.03  # taxa de crescimento de Apricoçildo em metros por ano
anos = 0  # contador de anos

while altura_a <= altura_j:
    anos += 1
    altura_j += taxa_cresc_j
    altura_a += taxa_cresc_a
    print(f"Ano {anos}: Josberanilson tem {altura_j:.2f}m e Apricoçildo tem {altura_a:.2f}m")

print(f"Apricoçildo ultrapassou Josberanilson após {anos} anos.")
altura_j = 1.50 
altura_a = 1.10 
taxa_cresc_j = 0.02 
taxa_cresc_a = 0.03  
anos = 0 

while altura_a <= altura_j:
    anos += 1
    altura_j += taxa_cresc_j
    altura_a += taxa_cresc_a
    print(f"Ano {anos}: Josberanilson tem {altura_j:.2f}m e Apricoçildo tem {altura_a:.2f}m")

print(f"Apricoçildo ultrapassou Josberanilson após {anos} anos.")
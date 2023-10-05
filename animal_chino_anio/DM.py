animals = {0: "Mono", 1: "Gallo", 2: "Perro", 3: "Cerdo", 4: "Rata", 5: "Buey", 6: "Tigre", 7: "Conejo", 8: "Dragón", 9: "Serpiente", 10: "Caballo", 11: "Cabra"}

año = 2022
print(f"El animal chino de {año} es {animals[año % 12]}")
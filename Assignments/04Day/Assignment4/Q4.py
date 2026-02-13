# 4. Weight conversion using lambda functions
tonns_to_kg = lambda t: t * 1000
kg_to_grams = lambda kg: kg * 1000
grams_to_mg = lambda g: g * 1000
mg_to_lbs = lambda mg: mg * 0.0000022046

tonns = float(input("Enter weight in tonns: "))
kg = tonns_to_kg(tonns)
grams = kg_to_grams(kg)
mg = grams_to_mg(grams)
lbs = mg_to_lbs(mg)

print(f"{kg} kg")
print(f"{grams} gm")
print(f"{mg} mg")
print(f"{lbs} lbs")

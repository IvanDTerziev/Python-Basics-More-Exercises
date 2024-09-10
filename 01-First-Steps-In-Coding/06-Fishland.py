price_mackerel = float(input())
price_sprat = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_mussels = int(input())

price_palamud = price_mackerel + (price_mackerel * 0.60)
sum_palamud = kg_palamud * price_palamud
price_safrid = price_sprat + (price_sprat * 0.80)
sum_safrid = kg_safrid * price_safrid
sum_mussels = kg_mussels * 7.50
total_sum = sum_palamud + sum_safrid + sum_mussels

print(f"{total_sum:.2f}")

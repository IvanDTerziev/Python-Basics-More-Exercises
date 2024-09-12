spring_prices = [("chrysanthemums", 2.00), ("roses", 4.10), ("tulips", 2.50)]
summer_prices = [("chrysanthemums", 2.00), ("roses", 4.10), ("tulips", 2.50)]
autumn_prices = [("chrysanthemums", 3.75), ("roses", 4.50), ("tulips", 4.15)]
winter_prices = [("chrysanthemums", 3.75), ("roses", 4.50), ("tulips", 4.15)]

prices = {
    "Spring": spring_prices,
    "Summer": summer_prices,
    "Autumn": autumn_prices,
    "Winter": winter_prices,
}

flower_indices = {"chrysanthemums": 0, "roses": 1, "tulips": 2}

chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

is_holiday = holiday == "Y"

chrysanthemums_price = prices[season][flower_indices["chrysanthemums"]][1]
roses_price = prices[season][flower_indices["roses"]][1]
tulips_price = prices[season][flower_indices["tulips"]][1]

total_price = chrysanthemums * chrysanthemums_price + \
              roses * roses_price + \
              tulips * tulips_price
if is_holiday:
    total_price *= 1 + 15 / 100

extra_discount = 0
if tulips > 7 and season == "Spring":
    extra_discount = 5 / 100
    total_price *= (1 - extra_discount)

if roses >= 10 and season == "Winter":
    extra_discount = 10 / 100
    total_price *= (1 - extra_discount)

if tulips+ roses + chrysanthemums > 20:
    extra_discount = 20 / 100
    total_price *= (1 - extra_discount)

total_price_final = total_price + 2

print(f"{total_price_final:.2f}")

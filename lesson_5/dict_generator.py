names = ["Mike", "Steven", "Amber", "Lucy", "Jan", ]
sallaries = [3500, 4300, 3760, 2900, 5100, ]
bonuses = ["10.15%", "15.50%", "14.30%", "11.40%", "13.70%", ]

dict_gen = {name: sallary * (1 + float(bonus[:-1]) / 100) for name, sallary, bonus in zip(names, sallaries, bonuses)}

for key, value in dict_gen.items():
    print(f" {key} have full sallary:  {round(value, 2)}")

# Weight converter
weight = float(input("Enter your weight: "))
weight_type_input = input("(K)gs or (L)bs: ")
kgs = ("k" or "K") in weight_type_input
lbs = ("l" or "L") in weight_type_input
ratio = 2.205
if (kgs):
    conversion = int(weight * ratio)
    print(str(conversion) + "Lbs")
else:
    conversion = int(weight // ratio)
    print(str(conversion) + "Kgs")
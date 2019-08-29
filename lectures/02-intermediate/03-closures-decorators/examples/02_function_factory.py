def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp

square = raise_to(2)
cube = raise_to(3)

print(square(12))
print(cube(3))

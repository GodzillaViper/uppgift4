# själva texten. 
test_string = input("Skriv en mening eller text: ")
# visar hur många ord i texten.
res = len(test_string.split())

# char.isdigit där char är en sifra som blir kontrolerad till true eller false. Sum är då den som summerar allt som är true. Hela saken kommer räkna hur mycket sifror finns i texten. 
numbers = sum(char.isdigit() for char in test_string)

# printar ut texten som visar antal ord och sifror. 
print(str(res))
print(str(numbers))



# själva texten. 
test_string = input("Skriv en mening eller text: ")
# visar hur många ord i texten.
res = len(test_string.split())

x_words=0 
words = test_string.split()
print(words)
for i in range(len(words)):
    for j in range(len(words[i])):
        if words [i][j].isdigit():
            x_words -=1
            break


# char.isdigit där char är en sifra som blir kontrolerad till true eller false. Sum är då den som summerar allt som är true. Hela saken kommer räkna hur mycket sifror finns i texten. 
numbers = sum(char.isdigit() for char in test_string)

# printar ut texten som visar antal ord och sifror. 
print(str(res + x_words))
print(str(numbers))


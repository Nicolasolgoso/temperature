frase_input =str(input("Tu frase para invertir:"))
frase_list = frase_input.split()

frase_list.reverse()

print(frase_list)
frase_output = " ".join(frase_list)
print(frase_output)
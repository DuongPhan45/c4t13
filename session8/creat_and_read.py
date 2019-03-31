animal = ['cat','dog','duck']
print (animal)
new_animal= input("inset an animal: ")
animal.append(new_animal)
print(animal)
print(*animal)
print(*animal, sep=',')
print(*animal, sep='|')
print(animal[0],animal[-1],animal[-2])

list = (animal[0].upper(),animal[-1].upper(),animal[-2].upper())
print(list)

# In cac phan tu cua list ra man hinh duoi cac hinh thuc khac nhau
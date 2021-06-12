motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
#substituir elementos na lista
motorcycles[0] = "ducati"
print(motorcycles)
#adicionar elementos a lista
motorcycles.append('triumph')
print(motorcycles)
#podemos colocar elementos no local onde quisermos, sem eliminar outros
motorcycles.insert(2, "motoguzzi")
print(motorcycles)
#podemos remover com o codigo del
del motorcycles[2]
print(motorcycles)

#podemos comecar com uma lista vazia e ir adicionando elementos
motas1 =[]
motas1.append("famel")
motas1.append("zontes")
motas1.append("vespa")
print(motas1)
#remove a item but use it in another list - .pop()
first_owned=motorcycles.pop(0)
print(f"the first motocycle I owned was a {first_owned.title()}")
#revmove a item from a list with a known value
print(motorcycles)
motorcycles.remove("triumph")
print(motorcycles)
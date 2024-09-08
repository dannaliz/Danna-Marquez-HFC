############################################################# Ejercicio 4
print((lambda x, y, z : x * y * z )(1,2,3))
print((lambda a : len(a)== 0 )([1,2]))
print((lambda a, n : len(a) >= n) ([1,2,3], 2))
print((lambda a : a ** 1/2 )(4))
print((lambda x, y : x.intersection(y))({1,2,3},{1,2}))

############################################################# Ejercicio 5

i = list(map(lambda x : x.upper(), filter(lambda x : "i" in str(x), (lambda t,x,y,z : t + x + y + z)([1,2,3,4],["Hackers","Fight","Club"],["Piccoro","Goku","Videl","Babidi","Broly"],["Python","Rust","Kotlin",""]))))
print(i)

############################################################# Ejercicio 6

par= [i for i in range (1,50) if  i%2 == 0 ]
impares = [i for i in range (1, 50) if i not in par]

x = [i for i in range (1,10) ]
lista = [(lambda i: i**2)(i) for i in x]

listaPro= [[1,2],[1,2,3]]
lista4 = [[i+1 for i in sublist] for sublist in listaPro]
print(lista4)
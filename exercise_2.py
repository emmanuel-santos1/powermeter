import json

repetidos = [1,2,3,"1","2","3",3,4,5]

r = [1,"5",2,"3"]

d_str = '{"valor":125.3,"codigo":123}'


# 1 Genere una lista con los valores no repetidos de la lista ‘repetidos’.
list(set(repetidos))

# 2 Genere una lista con los valores en común entre la lista ‘r’ y ‘repetidos’
list(set(r).intersection(set(repetidos)))

# 3 Transforme ‘d_str’ en un diccionario
json.load(d_str)

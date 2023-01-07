d = ['красный', 'оранжевый', 'жёлтый', 'зелёный', 'голубой', 'синий', 'фиолетовый']
print(id(d))
s = d
s.append('34')
print(id(s))
print(id(d))
print(s.pop())
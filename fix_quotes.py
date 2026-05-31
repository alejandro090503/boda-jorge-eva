with open('C:/Users/aleja/boda-jorge-eva/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

left  = c.count('\u201c')
right = c.count('\u201d')
print('Comillas izq: %d, der: %d' % (left, right))

c2 = c.replace('\u201c', '"').replace('\u201d', '"')

with open('C:/Users/aleja/boda-jorge-eva/index.html', 'w', encoding='utf-8') as f:
    f.write(c2)

print('Listo. %d comillas tipograficas corregidas.' % (left + right))

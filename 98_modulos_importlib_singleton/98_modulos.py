import importlib

import exemplo_m

print(exemplo_m.variavel)

for i in range(10):
    importlib.reload(exemplo_m)
    print(i)

print('Fim')
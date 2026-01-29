from sys import path
# print (*path, sep='\n')

import exemplo_99_packages.packages
from exemplo_99_packages.packages import soma_do_modulo
from exemplo_99_packages import packages
from exemplo_99_packages.packages import *

print(soma_do_modulo(1, 2))
print(exemplo_99_packages.packages.soma_do_modulo(1, 2))
print(packages.soma_do_modulo(1, 2))
print(variavel)

# Esse arquivo deve estar fora desta pasta para funcional.
# Para organição mantive ele na pasta.
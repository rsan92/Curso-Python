"""
Utilizamos o PIP (gerenciador de pacotes Python)
https://pypi.org

pip install nome-do-modulo
---
# Colorama
comando: pip install colorama
-
from colorama import init, Fore, Back, Style
init()

print(Back.BLUE)
print(Back.WHITE + Fore.RED + Style.BRIGHT + 'Alerta!')
print(Fore.GREEN + 'Passou!!')

# Openpyxl
comando: pip install openpyxl
#  pip install openpyxl
#  pip install python-pdf
import pydf
pdf = pydf.generate_pdf('<h1>Rafael Alves</h1>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)

"""
import platform
print(platform.architecture())

# import pydf
# pdf = pydf.generate_pdf('<h1>Rafael Alves</h1>')

with open('test_doc.pdf', 'w') as f:
    f.write('<h1>Rafael Alves</h1>')
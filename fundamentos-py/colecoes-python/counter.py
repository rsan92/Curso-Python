"""
lista = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 5, 66, 70]

res = Counter(lista)
print(res)
------
print(Counter('Rafael Sousa Alves Nobre'))
"""
from collections import Counter

texto = """
A Wikipédia é um projeto de enciclopédia colaborativa, universal e multilíngue estabelecido na internet sob o princípio 
wiki. Tem como propósito fornecer um conteúdo livre, objetivo e verificável​​, que todos possam editar e melhorar. 
O projeto é definido pelos princípios fundadores. O conteúdo é disponibilizado sob a licença Creative Commons BY-SA e 
pode ser copiado e reutilizado sob a mesma licença — mesmo para fins comerciais — desde que respeitando os termos e 
condições de uso.

Todos os editores da Wikipédia são voluntários. Eles integram uma comunidade colaborativa, sem um líder, na qual os 
membros coordenam os seus esforços no âmbito dos projetos temáticos e diversos espaços de discussão. Dentre as várias 
páginas de ajuda à disposição dos interessados em contribuir, estão as que explicam como criar um artigo ou editar um 
artigo. Em caso de dúvidas, não hesite em perguntar.

Todos podem publicar conteúdo on-line desde que sigam as regras básicas estabelecidas pela comunidade, como por exemplo
 a verificabilidade da informação ou notoriedade do tema. Debates e comentários sobre os artigos são bem-vindos. 
 As páginas de discussão servem para centralizar reflexões e avaliações sobre como melhorar o conteúdo da Wikipédia.
"""
palavras = texto.split()
res = Counter(palavras)
print(res.most_common(15))


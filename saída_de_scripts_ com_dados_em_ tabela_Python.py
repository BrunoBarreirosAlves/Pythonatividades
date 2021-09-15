# saída de scripts com dados em tabela Python
from tabulate import tabulate

planeta = ['Planeta', 'Raio (Km)', 'Massa (X 10^21 Kg)']
tabela = [
    ['Sol', 696000, 1989100000]
    ['Mercúrio', 2439, 330],
    ['Vênus', 6051, 641],
    ['Terra', 6371, 5973.6],
    ['Marte', 3390, 641.85],
    ['Júpiter', 69911, 1898600],
    ['Saturno', 58232, 568460],
    ['Urano', 25362, 86832],
    ['Neturno', 24622, 102430]]

print(tabulate(tabela, headers=planeta, tablefmt='fancy_grid'))

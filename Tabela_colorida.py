# saída de scripts com dados em tabela Python
from tabulate import tabulate
from termcolor import colored

def cria_planeta():
    planetas = ['Planeta', 'Raio (Km)', 'Massa (X 10^21 Kg)']

    return [colored(c, 'cyan', attrs=['bold']) for c in planetas]

def cria_tabela():
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

    return [
        [colored(d[0], 'yellow', attrs=['bold']), d[1], d[2]] for d in tabela
    ]

print(tabulate(cria_tabela(), headers=cria_planeta(), tablefmt='fancy_grid'))

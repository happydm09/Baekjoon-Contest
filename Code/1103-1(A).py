T = ['N.PO.', 'EO..P', 'WP..O', 'S.OP.']
F = ['NP..I', 'E.PI.', 'W.IP.', 'SI..P']
L = ['NP..O', 'E.PO.', 'W.OP.', 'SO..P']

S = input() + input() + input()

if S in T: print('T')
elif S in F: print('F')
elif S in L: print('Lz')
else: print('?')

import numpy as np




base = np.fromFile('./packet_base.txt', dtype=int, sep='\n')
weight = np.fromFile('./packet_weight.txt', dtype=float, sep='\n')

print(base * weight) 
print(np.split(base, len(base) / 8)[:4])
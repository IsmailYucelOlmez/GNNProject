import torch


DEVICE = "cpu"


SUPPORTED_EDGES = ["SINGLE", "DOUBLE", "TRIPLE", "AROMATIC"]


SUPPORTED_ATOMS = ["C", "N", "O", "F", "P", "S", "Cl", "Br", "I"]
ATOMIC_NUMBERS =  [6, 7, 8, 9, 15, 16, 17, 35, 53]


MAX_MOLECULE_SIZE = 20  


DISABLE_RDKIT_WARNINGS = True
import numpy as np

def open_pdb(file_location):
    """
    Returns the atom names and coordinates from a pdb file.

    The pdb file must specify the atom elements in the last column and follow
    the conventions outlined in the pdb format specification.

    Parameters
    ----------
    file_location : str
        Path of the pdb file to read.

    Returns
    -------
    symbols : list
        The atomic symbols in the pdb file.
    coords : np.ndarray
        The atomic coordinates in the pdb file.

    """

    with open(file_location) as f:
        data = f.readlines()

    coordinates = []
    symbols = []
    for line in data:
        if 'ATOM' in line[0:6] or 'HETATM' in line[0:6]:
            symbols.append(line[76:79].strip())
            atom_coords = [float(x) for x in line[30:55].split()]
            coordinates.append(atom_coords)

    coords = np.array(coordinates)
    
    return symbols, coords

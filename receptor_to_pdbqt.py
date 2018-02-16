#!/usr/bin/env python3

# Ricardo Avila
# Script for converting receptors to pdbqt using ODDT

import sys
import oddt
from oddt.docking.AutodockVina import write_vina_pdbqt

if len(sys.argv) != 4:
    print("Usage:", sys.argv[0], "<format> <receptor> <output_folder>")

else:
    file_type = sys.argv[1]
    receptor_file = sys.argv[2]
    path = sys.argv[3]

    # Read input molecule
    receptor = next(oddt.toolkit.readfile(file_type, receptor_file))
    # Calculate charges
    receptor.calccharges()
    # Write output 
    write_vina_pdbqt(receptor, path, flexible=False)

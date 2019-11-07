"""
molecool
A python package for analyzing and visualizing molecules.  For the MolSSI Best Practices Workshop.
"""

# Add imports here
from .functions import *
from .measure import calculate_angle, calculate_distance
from .molecule import build_bond_list
from .visualize import bond_histogram, draw_molecule
import molecool.io


# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions

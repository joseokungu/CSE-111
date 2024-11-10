"""
Program: chemistry
Author: Jose Okitandende
Purpose: Writing functions to calculate molar mass of substances
Date: 27/10/2024
IDE: Visual Studios Code
"""

from formula import parse_formula


# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

#EXTRA MILE: Index for molecule formula's names
FORMULA_NAME_INDEX = 0


def main():

    formula = str(input("Enter the molecular formula of the sample: "))
    weight = float(input("Enter the mass in grams of the sample: "))
    periodic_table_dict = make_periodic_table()
    symbol_quantity = parse_formula(formula, periodic_table_dict)
    molar_mass = compute_molar_mass(symbol_quantity, periodic_table_dict)
    moles = weight/molar_mass
    formula_name = get_formula_names(formula)

    print(f"Formula name: {formula_name}")
    print(f"Molar mass of glucose: {molar_mass} grams/mole")
    print(f"Number of moles in the sample: {round(moles, 5)} moles")
       

def make_periodic_table():
    periodic_table_dict = {
    # [symbol, name, atomic_mass]],
    "Ac":	["Actinium",	227],
    "Ag":	["Silver",	107.8682],
    "Al":	["Aluminum",	26.9815386],
    "Ar":	["Argon",	39.948],
    "As":	["Arsenic",	74.9216],
    "At":	["Astatine",	210],
    "Au":	["Gold",	196.966569],
    "B":    ["Boron",	10.811],
    "Ba":	["Barium",	137.327],
    "Be":	["Beryllium",	9.012182],
    "Bi":	["Bismuth",	208.9804],
    "Br":	["Bromine",	79.904],
    "C":    ["Carbon",	12.0107],
    "Ca":	["Calcium",	40.078],
    "Cd":	["Cadmium",	112.411],
    "Ce":	["Cerium",	140.116],
    "Cl":	["Chlorine",	35.453],
    "Co":	["Cobalt",	58.933195],
    "Cr":	["Chromium",	51.9961],
    "Cs":	["Cesium",	132.9054519],
    "Cu":	["Copper",	63.546],
    "Dy":	["Dysprosium",	162.5],
    "Er":	["Erbium",	167.259],
    "Eu":	["Europium",	151.964],
    "F":    ["Fluorine",	18.9984032],
    "Fe":	["Iron",	55.845],
    "Fr":	["Francium",	223],
    "Ga":	["Gallium",	69.723],
    "Gd":	["Gadolinium",	157.25],
    "Ge":	["Germanium",	72.64],
    "H":    ["Hydrogen",	1.00794],
    "He":	["Helium",	4.002602],
    "Hf":	["Hafnium",	178.49],
    "Hg":	["Mercury",	200.59],
    "Ho":	["Holmium",	164.93032],
    "I":    ["Iodine",	126.90447],
    "In":	["Indium",	114.818],
    "Ir":	["Iridium",	192.217],
    "K":    ["Potassium",	39.0983],
    "Kr":	["Krypton",	83.798],
    "La":	["Lanthanum",	138.90547],
    "Li":	["Lithium",	6.941],
    "Lu":	["Lutetium",	174.9668],
    "Mg":	["Magnesium",	24.305],
    "Mn":	["Manganese",	54.938045],
    "Mo":	["Molybdenum",	95.96],
    "N":    ["Nitrogen",	14.0067],
    "Na":	["Sodium",	22.98976928],
    "Nb":	["Niobium",	92.90638],
    "Nd":	["Neodymium",	144.242],
    "Ne":	["Neon",	20.1797],
    "Ni":	["Nickel",	58.6934],
    "Np":	["Neptunium",	237],
    "O":    ["Oxygen",	15.9994],
    "Os":	["Osmium",	190.23],
    "P":    ["Phosphorus",	30.973762],
    "Pa":	["Protactinium",	231.03588],
    "Pb":	["Lead",	207.2],
    "Pd":	["Palladium",	106.42],
    "Pm":	["Promethium",	145],
    "Po":	["Polonium",	209],
    "Pr":	["Praseodymium",	140.90765],
    "Pt":	["Platinum",	195.084],
    "Pu":	["Plutonium",	244],
    "Ra":	["Radium",	226],
    "Rb":	["Rubidium",	85.4678],
    "Re":	["Rhenium",	186.207],
    "Rh":	["Rhodium",	102.9055],
    "Rn":	["Radon",	222],
    "Ru":	["Ruthenium",	101.07],
    "S":    ["Sulfur",	32.065],
    "Sb":	["Antimony",	121.76],
    "Sc":	["Scandium",	44.955912],
    "Se":	["Selenium",	78.96],
    "Si":	["Silicon",	28.0855],
    "Sm":	["Samarium",	150.36],
    "Sn":	["Tin",	118.71],
    "Sr":	["Strontium",	87.62],
    "Ta":	["Tantalum",	180.94788],
    "Tb":	["Terbium",	158.92535],
    "Tc":	["Technetium",	98],
    "Te":	["Tellurium",	127.6],
    "Th":	["Thorium",	232.03806],
    "Ti":	["Titanium",	47.867],
    "Tl":	["Thallium",	204.3833],
    "Tm":	["Thulium",	168.93421],
    "U":    ["Uranium",	238.02891],
    "V":    ["Vanadium",	50.9415],
    "W":    ["Tungsten",	183.84],
    "Xe":	["Xenon",	131.293],
    "Y":    ["Yttrium",	88.90585],
    "Yb":	["Ytterbium",	173.054],
    "Zn":	["Zinc",	65.38],
    "Zr":	["Zirconium",	91.224],
    }
 
    return periodic_table_dict


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    total_mass = 0


    for inner_list in symbol_quantity_list:
        symbol = inner_list[SYMBOL_INDEX]
        quantity = inner_list[QUANTITY_INDEX]

        if symbol not in periodic_table_dict:
            print(f"Element {symbol} not found in the periodic table.")
            return None

        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
        total_mass += atomic_mass * quantity

    return total_mass

#### TESTS PASSED, AND SAMPLE RESULTS ARE MATCHING.
# EXTRA MILE:

def get_formula_names(formula):

    known_molecules_dict = {
        "Al2O3": "aluminum oxide",
        "CH3OH": "methanol",
        "C2H6O": "ethanol",
        "C2H5OH": "ethanol",
        "C3H8O": "isopropyl alcohol",
        "C3H8": "propane",
        "C4H10": "butane",
        "C6H6": "benzene",
        "C6H14": "hexane",
        "C8H18": "octane",
        "CH3(CH2)6CH3": "octane",
        "C13H18O2": "ibuprofen",
        "C13H16N2O2": "melatonin",
        "Fe2O3": "iron oxide",
        "FeS2": "iron pyrite",
        "H2O": "water",
        "C6H12O6": "glucose",
        "C10H16N2O3S": "penicillin",
        "C2H4O2": "acetic acid",
        "C3H6O": "acetone",
        "C3H4O2": "propionic acid",
        "C5H12": "pentane",
        "C7H8": "toluene",
        "C8H10": "xylene",
        "C10H14O": "camphor",
        "C12H22O11": "sucrose",
        "NaCl": "sodium chloride",
        "NH3": "ammonia",
        "HCl": "hydrochloric acid",
        "H2SO4": "sulfuric acid",
        "CO2": "carbon dioxide",
        "O2": "oxygen",
        "N2": "nitrogen",
        "H2": "hydrogen",
        "Cl2": "chlorine",
        "SO2": "sulfur dioxide",
        "NO2": "nitrogen dioxide",
        "CO": "carbon monoxide"
    }      

    if formula not in known_molecules_dict:
        name = "Unknown Compound"
    else:
        name = known_molecules_dict[formula]
    
    return name


if __name__ == "__main__":
    main()
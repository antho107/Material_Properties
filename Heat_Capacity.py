#Program will calculate heat capacity and internal energy following the Deybe Method
import numpy as np
import sys
import tkinter as tk

#Dictionaries of information (Deybe temp [K], MW [kg/kMol], Sommerfeld Parameter [J/(kmol-K^2)])
#Sommerfeld Parameters Ref: http://www.knowledgedoor.com/2/elements_handbook/electronic_heat_capacity_coefficient.html
#Need to find Sommerfeld Parameter for the following 
#"Argon": (85,39.948), "Diamond": (1850,12.01), "Germanium": (290,72.630), "Neon": (63,20.180)
Deybe_Dict = {"Aluminum": (390,26.982,1.35), "Beryllium": (980,9.0122,0.171), "Calcium": (230,40.078,2.73), 
              "Chromium": (440,51.996,1.42), "Copper": (310,63.546,0.69), "Gadolinium": (160,157.25,6.38),
              "Gold": (180,196.97,0.69), "Graphite": (1500,12.011,0.014), "Alpha_Iron": (430,55.85,4.9),
              "Gamma_Iron": (320,55.85,4.90), "Lead": (86,207.2,2.99), "Lithium": (430,6.94,1.65), "Mercury": (95,200.59,1.86), 
              "Molybdenum": (375,95.95,1.83), "Nickel": (375,58.693,7.04), "Niobium": (265,92.906,7.80), 
              "Platinum": (225,195.08,6.54), "Silver": (220,107.87,0.64), "Sodium": (160,22.990,1.38), "Tantalum": (245,180.95,5.87), 
              "White_Tin": (165,118.71,1.78), "Gray_Tin": (240,118.71,1.78), "Titanium": (350,47.867,3.36), 
              "Tungsten": (315,183.84,1.01), "Vanadium": (280,50.942,9.9), "Zinc": (250,65.38,0.64), "Zirconium": (280,91.224,2.77)}

Input_Dict = {}
C_Results_List_low = []
E_Results_List_low = []
C_Results_List_high = []
E_Results_List_high = []
mole_Weight_List = []

#Constants
h = 6.62607004081*(10**-34) #[J-s] Planck's Constant
kb = 1.3806485279*(10**-23) #[J/K] Boltzmann Constant
Ru = 8314.459848 #[J/kmol-K] Universal Gas Constant

######################################################################################################################################
#Refrence: https://drive.google.com/file/d/1stSdGIKIw-ao_-YWoB44wjBgOXDJpqKh/view
#Funciton will calculate the Deybe integral
def Deybe_E_est(xD):

    if xD < 0:
        Deybe_E_est = "Error Cannot be found"

    elif 0 < xD < 0.1:
        x2 = xD * xD
        Deybe_E_est = 1 - 0.375 * xD + x2 * (0.05 - 0.0005952380953 * x2)

    elif 0.1 <= xD < 7.25:
        Deybe_E_est =  ((((0.0946173 * xD - 4.432582) * xD + 85.07724) * xD - 800.6087) * xD + 3953.632) / ((((xD + 15.121491)
                        * xD + 143.155337) * xD + 682.0012) * xD + 3953.632)

    else:
        sum = 0
        N = 25 / xD
        if N > 0:
            xn = 1
            ex = np.exp(-xD)
            for i in np.arange(1, N):
                xn = xn * ex
                xi = i * xD
                sum = sum + xn * (6 + xi * (6 + xi * (3 + xi))) / (i**4)
                i += 1
        x2 = xD * xD
        Deybe_E_est = 3 * (6.493939402 - sum) / (xD * x2)

    return Deybe_E_est
######################################################################################################################################
#Determines Deybe temperature ratio
def Deybe_temp_ratio (Material, temp):
    Deybe_temperature = Deybe_Dict.get(Material)[0]
    xD = Deybe_temperature / temp
    return xD

#Calculate Phonon Contribution to heat capacity
def Calc_Deybe_Cp (Deybe_E_est, xD):
    Deybe_Cp = 3*Ru*((4*Deybe_E_est) - (3*xD)/(np.exp(xD)-1))
    return Deybe_Cp

#Calculate Electron Contribution to heat capacity
def Calc_Deybe_Ce (Material, temp):
    Sommerfeld_Parameter = Deybe_Dict.get(Material)[2]
    Deybe_Ce = Sommerfeld_Parameter*temp
    return Deybe_Ce

#Calculate Phonon Contrbution to Interal Energy
def Calc_Deybe_Eph (Deybe_E_est, temp):
    Deybe_Eph = 3*Ru*temp*Deybe_E_est
    return Deybe_Eph

#Calculate Electron Contribution to Internal Energy
def Calc_Deybe_Ee (Material, temp):
    Sommerfeld_Parameter = Deybe_Dict.get(Material)[2]
    Deybe_Ee = Sommerfeld_Parameter * (temp**2) / 2
    return Deybe_Ee

#Check inputs and make an input dictionary of materials and their respective mole fractions
def Check_Inputs():
    user_input = input("Enter a Material and its mole fraction, seperated by a comma:  ")
    if user_input == "CONTINUE":
        return "CONTINUE"
    else:
        try:
            user_input = tuple(user_input.split(","))
            material = user_input[0]
            mol_frac = float(user_input[1])

        except(IndexError):
            print("IndexError: Invalide indexing, separate inputs by a comma (,)")

        except(ValueError):
            print("ValueError: enter a material and its mole fraction separated by a comma (,)")
        
        finally:
            if material in Deybe_Dict.keys():
                try:
                    Input_Dict[material] = mol_frac
                except(UnboundLocalError):
                    print("UnboundLocalError: ensure a mole fraction has been entered")

            else:
                print("Enter a valide material")

#Calculates the sum of the inputted mole fractions, will check to ensure this is 1 in main program
def Check_Mole_Frac_Sum (Input_Dict):
    Mole_Fractions = Input_Dict.values()
    Mole_Frac_Sum = sum(Mole_Fractions)
    return Mole_Frac_Sum

#Calculates the mixture molecular weight
def Calc_Mix_Mol_Weigth (Deybe_Dict, Input_Dict):
    for k in Input_Dict: #k is the inputted material
        if k in Deybe_Dict.keys():
            mole_Frac = float(Input_Dict.get(k))
            null1, mole_Weight_Element, null2 = Deybe_Dict.get(k)
            mole_Weight = mole_Frac*mole_Weight_Element
            mole_Weight_List.append(mole_Weight)
        
        else:
            continue
        
        mole_Weight = sum(mole_Weight_List, 0)

    return mole_Weight

#######################################################################################################################################
#Main Program
print("Enter CONTINUE when all inputs have been entered")

#Generates input dictionary of elements and their respective mole fractions
while True:
    user_input = Check_Inputs()
    if user_input == "CONTINUE":
        break
    else:
        continue

#Check that the sum of the mole fractions is equal to 1
Mole_Frac_Sum = Check_Mole_Frac_Sum (Input_Dict)

if Mole_Frac_Sum == 1:
    print("Sum of the mole fractions is 1")
else:
    print("The sum of mole fraction must be equal to 1, currrently it is:   ", Mole_Frac_Sum)
    sys.exit()

print(Input_Dict)

temp_high = float(input("Eneter the upper temp bound:   "))
temp_low = float(input("Eneter the lower temp bound:   "))

#Low temperature results for heat capacity and internal energy
for k in Input_Dict: #k is the inputted material
    if k in Deybe_Dict.keys():
        mole_Frac = Input_Dict.get(k)
        xD = Deybe_temp_ratio(k, temp_low)
        Deybe_est = Deybe_E_est(xD)

        Deybe_Cp = Calc_Deybe_Cp(Deybe_est, xD)
        Deybe_Ce = Calc_Deybe_Ce(k, temp_low)
        Deybe_C = mole_Frac*(Deybe_Cp + Deybe_Ce)

        Deybe_Eph = Calc_Deybe_Eph(Deybe_est, temp_low)
        Deybe_Ee = Calc_Deybe_Ee(k, temp_low)
        Deybe_E = mole_Frac*(Deybe_Eph + Deybe_Ee)

        C_Results_List_low.append(Deybe_C) 
        E_Results_List_low.append(Deybe_E) 

    else:
        continue

C_temp_low = sum(C_Results_List_low, 0) #[J/(kmol-K)]
E_temp_low = sum(E_Results_List_low, 0) #[J/kmol]

#high temperature results for heat capacity and internal energy
for k in Input_Dict: #k is the inputted material
    if k in Deybe_Dict.keys():
        mole_Frac = Input_Dict.get(k)
        xD = Deybe_temp_ratio(k, temp_high)
        Deybe_est = Deybe_E_est(xD)

        Deybe_Cp = Calc_Deybe_Cp(Deybe_est, xD)
        Deybe_Ce = Calc_Deybe_Ce(k, temp_high)
        Deybe_C = mole_Frac*(Deybe_Cp + Deybe_Ce)

        Deybe_Eph = Calc_Deybe_Eph(Deybe_est, temp_high)
        Deybe_Ee = Calc_Deybe_Ee(k, temp_high)
        Deybe_E = mole_Frac*(Deybe_Eph + Deybe_Ee)

        C_Results_List_high.append(Deybe_C) 
        E_Results_List_high.append(Deybe_E) 

    else:
        continue

C_temp_high = sum(C_Results_List_high, 0) #[J/(kmol-K)]
E_temp_high = sum(E_Results_List_high, 0) #[J/kmol]

C_diffrence_mole = C_temp_high - C_temp_low #[J/(kmol-K)]
E_diffrence_mole = E_temp_high - E_temp_low #[J/(kmol-K)]

mole_Weight = Calc_Mix_Mol_Weigth (Deybe_Dict, Input_Dict)

C_diffrence = C_diffrence_mole / mole_Weight #[J/(kg-K)]
E_diffrence = E_diffrence_mole / mole_Weight #[J/kg]

print(mole_Weight, " [kg/kmol]")
print(C_diffrence_mole, " [J/(kmol-K)]")
print(E_diffrence_mole, " [J/kmol]")
print(C_diffrence, " [J/(kg-K)]")
print(E_diffrence, " [J/kg]")
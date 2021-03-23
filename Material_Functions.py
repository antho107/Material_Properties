import Material_Properties as MP
import numpy as np
#######################################################################################################################################
#Calculates Thermal Conductivity from NIST Data for Respective Material and temperature
def ThermalConductivity (Mat_Dict, temp):
    a, b, c, d, e, f, g, h, i = Mat_Dict.get("Thermal Conductivity").values() 
    Therm_Cond = function1(temp, a, b, c, d, e, f, g, h, i)  
    Mat_Prop_Updated = "Thermal Conductivity"  
    return Therm_Cond, Mat_Prop_Updated

#Calculates Specific Heat from NIST Data for Respective Material and temperature
def SpecificHeat (Mat_Dict, Material_Name, temp):
    if Material_Name == "SST316":
        if temp <= 50:
            a, b, c, d, e, f, g, h, i = Mat_Dict.get("Specific Heat 1").values()
            Mat_Prop_Updated = "Specific Heat 1"
        if temp > 50:
            a, b, c, d, e, f, g, h, i = Mat_Dict.get("Specific Heat 2").values() 
            Mat_Prop_Updated = "Specific Heat 2"           
    else:
            a, b, c, d, e, f, g, h, i = Mat_Dict.get("Specific Heat").values()  
            Mat_Prop_Updated = "Specific Heat"                  
    Spec_Heat =  function1(temp, a, b, c, d, e, f, g, h, i)  
    #Mat_Prop_Updated = "Specific Heat"       
    return Spec_Heat, Mat_Prop_Updated

#Calculates Youngs Modulus from NIST Data for Respective Material and temperature
def YoungsModulus (Mat_Dict, Material_Name, temp):
    if Material_Name == "SST304":
        if temp <= 57:
            a, b, c, d, e = Mat_Dict.get("Youngs Modulus Low Temp").values()
            Mat_Prop_Updated = "Youngs Modulus Low Temp"
        if temp > 57:
            a, b, c, d, e = Mat_Dict.get("Youngs Modulus High Temp").values()
            Mat_Prop_Updated = "Youngs Modulus High Temp"
    if Material_Name == "SST316":
        if temp <= 50:
            a, b, c, d, e = Mat_Dict.get("Youngs Modulus Low Temp").values()
            Mat_Prop_Updated = "Youngs Modulus Low Temp"
        if temp > 50:
            a, b, c, d, e = Mat_Dict.get("Youngs Modulus High Temp").values()
            Mat_Prop_Updated = "Youngs Modulus High Temp"
    if Material_Name == "INVAR":
            a, b, c, d, e = Mat_Dict.get("Youngs Modulus").values()
            Mat_Prop_Updated = "Youngs Modulus"
    Youngs_Mod = function2(temp, a, b, c, d, e)
    return Youngs_Mod, Mat_Prop_Updated

#Calculates Linear Expansion from NIST Data for Respective Material and temperature
def LinearExpansion (Mat_Dict, temp):
    a, b, c, d, e = Mat_Dict.get("Linear Expansion").values()
    Linear_Exp = function2(temp, a, b, c, d, e)
    Mat_Prop_Updated = "Linear Expansion"
    return Linear_Exp, Mat_Prop_Updated

#Funciton for Thermal Conductivity and Specific Heat
def function1 (temp, a, b, c, d, e, f, g, h, i):
    func1 = 10**(a + b*(np.log10(temp)) + c*(np.log10(temp))**2 + d*(np.log10(temp))**3 + e*(np.log10(temp))**4 
        + f*(np.log10(temp))**5 + g*(np.log10(temp))**6 + h*(np.log10(temp))**7 + i*(np.log10(temp))**8)  
    return func1

#Funciton for Young's Modulus and Linear Expansion
def function2 (temp, a, b, c, d, e):
    func2 = a + b*temp + c*(temp**2) + d*(temp**3) + e*(temp**4)
    return func2

#Funciton will get the dictionary corresponding to the inputted material name
def GetCorrectDict (Material_Name):
    if Material_Name == "SST304":
        Mat_Dict = MP.SST304Dict
        temp_Dict = MP.SST304TempBoundsDict
    if Material_Name == "SST304L":
        Mat_Dict = MP.SST304LDict
        temp_Dict = MP.SST304LTempBoundsDict        
    if Material_Name == "SST316":
        Mat_Dict = MP.SST316Dict
        temp_Dict = MP.SST316TempBoundsDict
    if Material_Name == "INVAR":
        Mat_Dict = MP.InvarDict
        temp_Dict = MP.InvarTempBoundsDict   
    return Mat_Dict, temp_Dict       

def CheckTempBounds (Mat_Prop_Updated, temp_Dict, temp):
    bounds = temp_Dict.get(Mat_Prop_Updated)
    low, high = bounds[0], bounds[1]
    if temp >= low and temp <= high:
        return True
    else:
        return False
#######################################################################################################################################
#Main Program
#Program will determine material properies given temperaure a material name
Acceptable_Materials_List = ["SST304", "SST304L", "SST316", "INVAR"]
Acceptable_Material_Property_List = ["THERMAL CONDUCTIVITY", "SPECIFIC HEAT", "YOUNGS MODULUS", "LINEAR EXPANSION"]

while True:
    Material_Name = input("Enter a material (SST304, SST304L, SST316, Invar):   ").upper()
    if Material_Name in Acceptable_Materials_List:
        break
    else:
        print("Enter an acceptable material")

while True:
    Mat_Prop = input("Enter a material property (Thermal Conductivity, Specific Heat, Youngs Modulus, Linear Expansion):   ").upper()
    if Mat_Prop in Acceptable_Material_Property_List:
        break
    else:
        print("Enter an acceptable material property")

#Get corresponding material dictionaries
Mat_Dict, temp_Dict = GetCorrectDict (Material_Name)

#Calculate specified material property
while True:
    if Mat_Prop == "THERMAL CONDUCTIVITY":
        temp = float(input("Enter a temperature in Kelvin:   "))
        Therm_Cond, Mat_Prop_Updated = ThermalConductivity(Mat_Dict, temp)
        if CheckTempBounds(Mat_Prop_Updated, temp_Dict, temp):
            print("The Theraml Conductivity is: ",round(ThermalConductivity(Mat_Dict,temp)[0],3), "[W/(m-K)]")
            break
        else:
            print("Entered temperature is outside of bounds", temp_Dict.get(Mat_Prop_Updated))

    if Mat_Prop == "SPECIFIC HEAT":
        temp = float(input("Enter a temperature in Kelvin:   "))
        Therm_Cond, Mat_Prop_Updated = ThermalConductivity(Mat_Dict, temp)
        if CheckTempBounds(Mat_Prop_Updated, temp_Dict, temp):
            print("The Specific Heat is: ",round(SpecificHeat(Mat_Dict, Material_Name, temp)[0],3), "[J/(kg-K)]")
            break
        else:
            print("Entered temperature is outside of bounds", temp_Dict.get(Mat_Prop_Updated))

    if Mat_Prop == "YOUNGS MODULUS":
        temp = float(input("Enter a temperature in Kelvin:   "))
        Therm_Cond, Mat_Prop_Updated = ThermalConductivity(Mat_Dict, temp)
        if CheckTempBounds(Mat_Prop_Updated, temp_Dict, temp):
            print("The Young's Modulus is: ",round(YoungsModulus(Mat_Dict, Material_Name, temp)[0],3), "[GPa]")
            break
        else:
            print("Entered temperature is outside of bounds", temp_Dict.get(Mat_Prop_Updated))

    if Mat_Prop == "LINEAR EXPANSION":
        temp = float(input("Enter a temperature in Kelvin:   "))
        Therm_Cond, Mat_Prop_Updated = ThermalConductivity(Mat_Dict, temp)
        if CheckTempBounds(Mat_Prop_Updated, temp_Dict, temp):
            print("The Linear Expansion is: ",round(LinearExpansion(Mat_Dict, temp)[0],3), "[m/m]")
            break
        else:
            print("Entered temperature is outside of bounds", temp_Dict.get(Mat_Prop_Updated))
#######################################################################################################################################
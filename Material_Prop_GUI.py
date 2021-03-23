from tkinter import *
import Material_Properties as MP
import numpy as np

#######################################################################################################################################
#PYTHON funcitons from Material_Funcitons.py
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
    if Material_Name == "Invar":
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
    if Material_Name == "Invar":
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
#TKinder Funcitons
def button_clear():
    Answer_Entry.delete(8,END)
    temperature_entry.delete(21,END)

def button_answer():
    temp = temperature_entry.get()[21:]
    temp = int(temp)
    prop = selected_prop.get()
    mat = selected_mat.get()

    global Mat_Dict
    global temp_Dict

    Mat_Dict, temp_Dict = GetCorrectDict (mat)

    if prop == "Thermal Conductivity":
        null, Mat_Prop_Updated = ThermalConductivity(Mat_Dict, temp)
        if CheckTempBounds(Mat_Prop_Updated, temp_Dict, temp):
            final_answer = round(ThermalConductivity(Mat_Dict,temp)[0],3)
            final_answer = str(final_answer)
            Answer_Entry.delete(8, END)
            Answer_Entry.insert(8, final_answer + " [W/(m-K)]")
        else:
            temp_bounds = str(temp_Dict.get(Mat_Prop_Updated))
            Answer_Entry.delete(8, END)
            Answer_Entry.insert(8, "Entered temperature is outside of bounds" + temp_bounds)

    if prop == "Specific Heat":
        null, Mat_Prop_Updated = SpecificHeat(Mat_Dict, mat, temp)
        if CheckTempBounds(Mat_Prop_Updated, temp_Dict, temp):
            final_answer = round(SpecificHeat(Mat_Dict, mat, temp)[0],3)
            final_answer = str(final_answer)
            Answer_Entry.delete(8, END)
            Answer_Entry.insert(8, final_answer + " [J/(kg-K)]")
        else:
            temp_bounds = str(temp_Dict.get(Mat_Prop_Updated))
            Answer_Entry.delete(8, END)
            Answer_Entry.insert(8, "Entered temperature is outside of bounds" + temp_bounds)

    if prop == "Youngs Modulus":
        null, Mat_Prop_Updated = YoungsModulus(Mat_Dict, mat, temp)
        if CheckTempBounds(Mat_Prop_Updated, temp_Dict, temp):
            final_answer = round(YoungsModulus(Mat_Dict, mat, temp)[0],3)
            final_answer = str(final_answer)
            Answer_Entry.delete(8, END)
            Answer_Entry.insert(8, final_answer + " [GPa]")
        else:
            temp_bounds = str(temp_Dict.get(Mat_Prop_Updated))
            Answer_Entry.delete(8, END)
            Answer_Entry.insert(8, "Entered temperature is outside of bounds" + temp_bounds)

    if prop == "Linear Expansion":
        null, Mat_Prop_Updated = LinearExpansion(Mat_Dict, temp)
        if CheckTempBounds(Mat_Prop_Updated, temp_Dict, temp):
            final_answer = round(LinearExpansion(Mat_Dict,temp)[0],10)
            final_answer = str(final_answer)
            Answer_Entry.delete(8, END)
            Answer_Entry.insert(8, final_answer + " [m/m]")
        else:
            temp_bounds = str(temp_Dict.get(Mat_Prop_Updated))
            Answer_Entry.delete(8, END)
            Answer_Entry.insert(8, "Entered temperature is outside of bounds" + temp_bounds)
##################################################################################################################################### 
#Code for TKinder window, buttons, entries, etc...
root = Tk()

root.title("Material Property Calc")

#Temperature Input
temperature_entry = Entry(root, width=60, borderwidth=5)
temperature_entry.insert(0, "Enter a Temp (in K): ")

#decalre tkiner variables
selected_prop = StringVar()
selected_mat = StringVar()

#Set default
selected_prop.set("Thermal Conductivity")
selected_mat.set("SST304")

#Drop Down Menu
drop_Property = OptionMenu(root, selected_prop, "Thermal Conductivity", "Specific Heat", "Youngs Modulus", "Linear Expansion")
drop_Material = OptionMenu(root, selected_mat, "SST304", "SST304L", "SST316", "Invar")
#Answer Box
Answer_Entry = Entry(root, width=60, borderwidth=5)
Answer_Entry.insert(0,"Answer: ",)
#Clear Button
Clear_Button = Button(root, text = "Clear All", padx=10, pady=5, command= button_clear)
Answer_Button = Button(root, text = "Calc", padx=10, pady=5, command= button_answer)

#Put on window
temperature_entry.grid(row=0, column=0, columnspan=2)
drop_Property.grid(row=1, column=0, columnspan=2)
drop_Material.grid(row=2, column=0, columnspan=2)
Answer_Entry.grid(row=3, column=0, columnspan=2)
Clear_Button.grid(row=4, column=0, columnspan=2)
Answer_Button.grid(row = 3, column=5)

root.mainloop()

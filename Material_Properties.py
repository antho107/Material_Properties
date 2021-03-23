#list = [SST3041, SST3042, ...]
#Material Data from NIST
SST304Dict = {"Thermal Conductivity": {"a":-1.4087, "b":1.3982, "c":0.2543, "d":-0.6260, "e":0.2334, "f":0.4256, "g":-0.4658, "h":0.1650, "i":-0.0199}, 
              "Specific Heat": {"a":22.0061, "b":-127.5528, "c":303.647, "d":-381.0098, "e":274.0328, "f":-112.9212, "g":24.7593, "h":-2.239153, "i":0},
              "Youngs Modulus High Temp": {"a":210.0593, "b":0.1534883, "c":-0.001617390, "d":0.000005117060, "e":-0.000000006154600},
              "Youngs Modulus Low Temp": {"a":209.8145, "b":0.1217019, "c":-0.01146999, "d":0.0003605430, "e":-0.000003017900},
              "Linear Expansion": {"a":-295.54e-5, "b":-0.39811e-5, "c":0.0092683e-5, "d":-0.000020261e-5, "e":0.000000017127e-5}}

SST304LDict = {"Thermal Conductivity": {"a":-1.4087, "b":1.3982, "c":0.2543, "d":-0.6260, "e":0.2334, "f":0.4256, "g":-0.4658, "h":0.1650, "i":-0.0199}, 
              "Specific Heat": {"a":-351.51, "b":3123.695, "c":-12017.28, "d":26143.99, "e":-35176.33, "f":29981.75, "g":-15812.78, "h":4719.64, "i":-610.515},
              "Linear Expansion": {"a":-295.54e-5, "b":-0.39811e-5, "c":0.0092683e-5, "d":-0.000020261e-5, "e":0.000000017127e-5}}

SST316Dict = {"Thermal Conductivity": {"a":-1.4087, "b":1.3982, "c":0.2543, "d":-0.6260, "e":0.2334, "f":0.4256, "g":-0.4658, "h":0.1650, "i":-0.0199}, 
              "Specific Heat 1": {"a":12.2486, "b":-80.6422, "c":218.743, "d":-308.854, "e":239.5296, "f":-89.9982, "g":3.15315, "h":8.44996, "i":-1.91368},
              "Specific Heat 2": {"a":-1879.464, "b":3643.198, "c":76.70125, "d":-6176.028, "e":7437.6247, "f":-4305.7217, "g":1382.4627, "h":-237.22704, "i":17.05262},
              "Youngs Modulus High Temp": {"a":2.079488e2, "b":7.394241e-2, "c":-9.627200e-4, "d":2.845560e-6, "e":-3.240800e-9},
              "Youngs Modulus Low Temp": {"a":2.084729e2, "b":-1.358965e-1, "c":8.368629e-3, "d":-1.381700e-4, "e":6.831930e-7},
              "Linear Expansion": {"a":-295.54e-5, "b":-0.39811e-5, "c":0.0092683e-5, "d":-0.000020261e-5, "e":0.000000017127e-5}}

InvarDict = {"Thermal Conductivity": {"a":-2.7064, "b":8.5191, "c":-15.923, "d":18.276, "e":-11.9116, "f":4.40318, "g":-0.86018, "h":0.068508, "i":0}, 
              "Specific Heat": {"a":28.08, "b":-228.23, "c":777.587, "d":-1448.423, "e":1596.567, "f":-1040.294, "g":371.2125, "h":-56.004, "i":0},
              "Youngs Modulus": {"a":1.41565e2, "b":2.54435e-2, "c":-1.00842e-3, "d":6.72797e-6, "e":-1.08230e-8},
              "Linear Expansion": {"a":-52.65e-5, "b":0.01009e-5, "c":0.0008395e-5, "d":-0.000001973e-5, "e":0.00000000008794e-5}}

#Temperature bounds (Dicitony, key is property, vales are touple of bounds)
SST304TempBoundsDict = {"Thermal Conductivity": (1,300), "Specific Heat": (4,300), "Youngs Modulus Low Temp": (5,57), 
                        "Youngs Modulus High Temp": (57,293), "Linear Expansion": (4,300)}

SST304LTempBoundsDict = {"Thermal Conductivity": (1,300), "Specific Heat": (4,23), "Linear Expansion": (4,300)}

SST316TempBoundsDict = {"Thermal Conductivity": (1,300), "Specific Heat 1": (4,50), "Specific Heat 2": (50,300), 
                        "Youngs Modulus Low Temp": (8,50), "Youngs Modulus High Temp": (50,294), "Linear Expansion": (4,300)}

InvarTempBoundsDict = {"Thermal Conductivity": (4,300), "Specific Heat": (4,27), 
                        "Youngs Modulus": (3,298), "Linear Expansion": (4,300)}                   
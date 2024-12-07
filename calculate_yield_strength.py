#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Name: calculate_yield_strength.py
Author: farid fattahpour
Date: [2024-12-06]
Description:
    This script uses the Thermo-Calc Python (tc_python) library to calculate 
    the yield strength of an alloy at a given temperature and composition. 
    It configures a system with a specified database, selects elements, sets 
    arguments for a yield strength property model, and finally prints the 
    available result quantities.

Requirements:
    - tc_python package
    - A valid Thermo-Calc license and database (TCHEA6 in this example).

Usage:
    python3 calculate_yield_strength.py
"""

import os
import sys
from tc_python import TCPython, CompositionUnit

def main():
    # Initial conditions
    # Temperature: 973 K, converted to °C as a reference
    # (The property model will be set in Kelvin, so we add back 273.15 later.)
    temperature_k = 973
    temperature_c = temperature_k - 273.15  # 700°C equivalent
    dependent_element = "Ni"
    composition = {"Co": 26.2, "Cr": 35.67}

    # Create a session with Thermo-Calc
    try:
        with TCPython() as session:
            # Set cache folder based on the script name
            cache_folder = os.path.splitext(os.path.basename(__file__))[0] + "_cache"
            system = (session
                      .set_cache_folder(cache_folder)
                      .select_database_and_elements("TCHEA6", [dependent_element] + list(composition.keys()))
                      .get_system())

            # Print available property models
            print("Available property models:", session.get_property_models())

            # Select the property model "Yield Strength"
            calc = system.with_property_model_calculation("Yield Strength")

            # Set temperature in Kelvin
            calc.set_temperature(temperature_k)  
            calc.set_composition_unit(CompositionUnit.MOLE_PERCENT)
            
            # Set composition
            for element, value in composition.items():
                calc.set_composition(element, value)

            # Print available arguments for the property model
            print("Available arguments:", calc.get_arguments())

            # Set arguments for the yield strength calculation
            calc.set_argument("Solid solution strengthening temperature", "700")
            calc.set_argument("User_Hall_Petch_selection", "True")
            calc.set_argument("grain_str_selection", "True")
            calc.set_argument("sol_str_selection", "True")
            calc.set_argument("Grain size in mu", "15")
            calc.set_argument("Hall_Petch constant", "653.55")
            calc.set_argument("Constant strength addition", "10")
            calc.set_argument("Matrix", "FCC_L12")

            # Perform the calculation
            result = calc.calculate()

            # Print available result quantities
            print("Available result quantities:", result.get_result_quantities())
            
            # (Optionally, retrieve and print the yield strength result if known)
            # yield_strength = result.get_value("<result_key>")
            # print("Calculated Yield Strength:", yield_strength)

    except Exception as e:
        print("An error occurred during the calculation:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()

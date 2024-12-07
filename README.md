# Yield Strength Calculation using Thermo-Calc Python

This repository contains a Python script that demonstrates how to calculate the yield strength of a specified alloy composition using the Thermo-Calc Python (tc_python) API. It sets up the thermodynamic system, selects the property model, configures the required parameters, and prints out the available results.

## Features

- **Thermo-Calc Integration:** Utilize the tc_python API to access the TCHEA6 database and perform property model calculations.
- **Yield Strength Calculation:** Set custom arguments (temperature, composition, grain size, Hall-Petch constants, and other relevant parameters) to calculate the yield strength of an alloy.
- **Customizable:** Easily modify the composition, temperature, or other arguments in the script to suit your needs.
- **Informative Output:** Prints available property models, arguments, and result quantities to help guide further customization.

## Requirements

- **Software:**
  - Python 3.6+
  - Thermo-Calc Software with a valid license
  - The `tc_python` Python package (provided by Thermo-Calc)
  
- **Database:**
  - Access to the `TCHEA6` database (or a suitable equivalent) is assumed. Modify the database name in the script if a different one is required.

## Installation

1. **Thermo-Calc Python Installation:**  
   Please refer to the official Thermo-Calc documentation for instructions on installing `tc_python` and configuring your license.

2. **Clone This Repository:**
   ```bash
   git clone https://github.com/faridf/yield-strength-calculation.git
   cd yield-strength-calculation
   ```
3. **(Optional) Create a Virtual Environment:**
   ```bash
    python3 -m venv env
    source env/bin/activate
    ```
4. **Install Requirements (if any are listed in requirements.txt):**
      ```bash
      pip install -r requirements.txt
      ```

## Usage

Run the script:

```python
python3 calculate_yield_strength.py
 ```
The script sets the alloy composition (Ni-Co-Cr system), temperature, and other model parameters.
It then prints out:
  1. Available property models
  2. Available arguments for the selected model
  3. Available result quantities after the calculation
You can modify the composition, temperature, and arguments directly in the script to suit your specific scenario.


## Customization

Composition:
Change the composition dictionary in calculate_yield_strength.py to set new element concentrations.

Temperature:
Modify the temperature_k variable to run calculations at different temperatures.

Model Arguments:
Adjust the .set_argument() calls to select different strengthening mechanisms or constants.



   

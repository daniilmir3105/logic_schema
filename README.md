# Logic Circuits Simulation

This project implements two logical circuits based on the provided schematic descriptions. Users can input their own values to simulate the circuits and get the output results. The program includes input validation to ensure correct usage.

---

## Features
- Simulation of two logical circuits:
  - **Circuit 1**: Produces outputs `P` and `S` based on inputs `a` and `b`.
  - **Circuit 2**: Produces output `Y` based on inputs `X1`, `X2`, and `X3`.
- Input validation ensures that all inputs are either `0` or `1` and that the correct number of inputs is provided.
- User-friendly error messages for invalid input.

---

## Circuit Descriptions
### Circuit 1
- **Inputs**: `a` and `b`
- **Logic**:
  1. `element_1 = NOT (a AND b)`
  2. `element_2 = NOT (a AND element_1)`
  3. `element_3 = NOT (element_1 AND b)`
  4. `element_4 = NOT element_1`
  5. `element_5 = NOT (element_2 AND element_3)`
- **Outputs**:
  - `P = element_4`
  - `S = element_5`

### Circuit 2
- **Inputs**: `X1`, `X2`, and `X3`
- **Logic**:
  1. `element_1 = X2 OR X3`
  2. `element_2 = X2 OR X1`
  3. `element_3 = NOT element_1`
  4. `element_4 = X3 AND element_2`
  5. `element_5 = element_3 OR element_4`
- **Output**:
  - `Y = element_5`

---

## Requirements
- Python 3.6 or higher

---

## How to Use
1. Clone or download the repository.
2. Run the program using:
   ```bash
   python logic_circuits.py
   ```
3. Follow the prompts to input the required values:
   - For **Circuit 1**, input two values (`a` and `b`).
   - For **Circuit 2**, input three values (`X1`, `X2`, and `X3`).
4. The program will validate the inputs and display the outputs for each circuit.

---

## Example Usage
### Circuit 1:
**Input:**
```
Enter two values for a and b (0 or 1): 1 0
```
**Output:**
```
Results for Circuit 1: P = True, S = True
```

### Circuit 2:
**Input:**
```
Enter three values for X1, X2, and X3 (0 or 1): 1 1 0
```
**Output:**
```
Result for Circuit 2: Y = True
```

---

## Input Validation
- The program ensures that:
  - All inputs are integers (`0` or `1`).
  - The correct number of inputs is provided for each circuit.
- If the input is invalid, the user will be prompted to try again with a clear error message.

---

## Project Structure
- `logic_circuits.py`: Main script containing the implementation of the circuits and input handling.

---

## License
This project is open-source and available under the MIT License.


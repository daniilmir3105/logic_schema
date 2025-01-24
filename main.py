# Implementation of the first circuit
def circuit_1(a, b):
    # Circuit elements
    element_1 = not (a and b)  # AND-NOT
    element_2 = not (a and element_1)  # AND-NOT
    element_3 = not (element_1 and b)  # AND-NOT
    element_4 = not element_1  # AND-NOT
    element_5 = not (element_2 and element_3)  # AND-NOT

    # Outputs
    P = element_4
    S = element_5
    return P, S


# Implementation of the second circuit
def circuit_2(X1, X2, X3):
    # Circuit elements
    element_1 = X2 or X3  # OR
    element_2 = X2 or X1  # OR
    element_3 = not element_1  # Inverter (NOT)
    element_4 = X3 and element_2  # AND
    element_5 = element_3 or element_4  # OR

    # Output
    Y = element_5
    return Y


# Input validation function
def get_inputs(prompt, num_inputs):
    while True:
        try:
            inputs = input(prompt).split()
            if len(inputs) != num_inputs:
                print(f"Please enter exactly {num_inputs} values separated by spaces.")
                continue
            # Convert inputs to integers and ensure they are 0 or 1
            inputs = [int(value) for value in inputs]
            if all(value in [0, 1] for value in inputs):
                return inputs
            else:
                print("All values must be either 0 or 1.")
        except ValueError:
            print("Invalid input. Please enter only integers 0 or 1.")


# Main execution
if __name__ == "__main__":
    print("Circuit 1:")
    # Get inputs for Circuit 1
    a, b = get_inputs("Enter two values for a and b (0 or 1): ", 2)
    P, S = circuit_1(a, b)
    print(f"Results for Circuit 1: P = {P}, S = {S}")

    print("\nCircuit 2:")
    # Get inputs for Circuit 2
    X1, X2, X3 = get_inputs("Enter three values for X1, X2, and X3 (0 or 1): ", 3)
    Y = circuit_2(X1, X2, X3)
    print(f"Result for Circuit 2: Y = {Y}")

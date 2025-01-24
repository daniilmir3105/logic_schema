# Implementation of the first circuit
def scheme_1(a, b):
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
def scheme_2(X1, X2, X3):
    # Circuit elements
    element_1 = X2 or X3  # OR
    element_2 = X2 or X1  # OR
    element_3 = not element_1  # Inverter (NOT)
    element_4 = X3 and element_2  # AND
    element_5 = element_3 or element_4  # OR

    # Output
    Y = element_5
    return Y


# Usage examples
if __name__ == "__main__":
    # Example for the first circuit
    a, b = 1, 0  # Input values
    P, S = scheme_1(a, b)
    print(f"Results for Schema 1: P = {P}, S = {S}")

    # Example for the second circuit
    X1, X2, X3 = 0, 1, 1  # Input values
    Y = scheme_2(X1, X2, X3)
    print(f"Result for Schema 2: Y = {Y}")

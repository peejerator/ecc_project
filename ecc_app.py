import numpy as np
import matplotlib.pyplot as plt

def check_correct(prompt: str = "Is this correct? (yes/no)") -> bool:
    """
    Ask the user to confirm if the displayed parameters are correct.
    Returns True if the parameters are correct, otherwise False.
    """
    print(prompt, end=' ')
    while True:
        confirmation = input().strip().lower()
        if confirmation in ['yes', 'y', '']:
            return True
        elif confirmation in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please answer with 'yes' or 'no'.")

def get_curve_params() -> tuple:
    """
    Get the coefficients of the elliptic curve from the user.
    The curve is defined by the equation y^2 = x^3 + ax + b.
    The coefficients a and b must be such that the curve is non-singular.
    """
    print("Please enter the parameters for the elliptic curve y^2 = x^3 + ax + b:")
    while True:
        try:
            a = float(input("Enter the coefficient a: "))
            b = float(input("Enter the coefficient b: "))
        except ValueError:
            print("Invalid input. Please enter numeric values for coefficients a and b.")

        if 4*a**3 + 27*b**2 == 0:
            print("The curve is singular (not valid). Please enter different coefficients.")
            continue

        print(f"Using the elliptic curve: y^2 = x^3 + {a}x + {b}")
        if check_correct():
            break

    return a, b

def get_points(a, b) -> tuple:
    """
    Get the points from the user.
    Returns the points P and Q on the curve.
    """
    print("Please enter the first point on the curve P as (x, y):", end=' ')
    while True:
        try:
            x1, y1 = map(float, input().strip().strip('()').strip().split(','))
            if y1**2 == x1**3 + a*x1 + b:
                print(f"P = ({x1}, {y1})")
                if check_correct():
                    break
            else:
                print("The point does not lie on the curve. Please enter a valid point.")
        except (ValueError, TypeError):
            print("Invalid input. Please enter two numeric values for the point (x, y).", end=' ')

    print("Please enter the second point on the curve Q as (x, y):", end=' ')
    while True:
        try:
            x2, y2 = map(float, input().strip().strip('()').strip().split(','))
            if y2**2 == x2**3 + a*x2 + b:
                print(f"Q = ({x2}, {y2})")
                if check_correct():
                    break
            else:
                print("The point does not lie on the curve. Please enter a valid point (x, y):", end=' ')
        except (ValueError, TypeError):
            print("Invalid input. Please enter two numeric values for the point (x, y):", end=' ')

    return (x1, y1), (x2, y2)

def add_points(P, Q, a):
    """
    Add two points P and Q on the elliptic curve defined by y^2 = x^3 + ax + b.
    Returns the resulting point R = P + Q.
    """
    if (P == Q and P[1] == 0) or (P[0] == Q[0] and P[1] == -Q[1]):
        # Point at infinity (identity element)
        return (None, None)
    elif P == Q:
        # Point doubling
        x1, y1 = P
        m = (3 * x1**2 + a) / (2 * y1)
    else:
        # Point addition
        x1, y1 = P
        x2, y2 = Q
        m = (y2 - y1) / (x2 - x1)

    x3 = m**2 - x1 - x2
    y3 = m * (x1 - x3) - y1

    return (x3, y3)

def draw_result(a, b, P, Q, R):
    """
    Draw the elliptic curve and the points P, Q, and R.
    """
    x = np.linspace(-10, 10, 400)
    # get y values without causing RuntimeWarning for negative values
    x = x[x**3 + a*x + b >= 0]
    y = np.sqrt(x**3 + a*x + b)
    y_neg = -y

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='y^2 = x^3 + ax + b', color='blue')
    plt.plot(x, y_neg, color='blue')

    m = (Q[1] - P[1]) / (Q[0] - P[0]) if P != Q else (3 * P[0]**2 + a) / (2 * P[1])

    # Draw the line connecting P and Q (going off to infinity)
    x_line = np.linspace(-10, 10, 400)
    y_line = m * (x_line - P[0]) + P[1]
    plt.plot(x_line, y_line, color='orange', label='Line through P and Q')

    # Plot points P, Q, and R
    plt.scatter(*P, color='red', label='Point P')
    plt.scatter(*Q, color='blue', label='Point Q')
    plt.scatter(*R, color='green', label='Point R')

    plt.title('Elliptic Curve and Points')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.grid()
    plt.legend()
    plt.show()

def main():
    print("Welcome to the ECC App!")
    a, b = get_curve_params()
    while True:
        print(f"Using the elliptic curve: y^2 = x^3 + {a}x + {b}")
        P, Q = get_points(a, b)
        R = add_points(P, Q, a)
        print(f"The result of adding points P and Q is R = {R if R[0] is not None else 'Point at infinity'}")
        if R[0] is not None:
            draw_result(a, b, P, Q, R)

        if not check_correct("Would you like to add another pair of points? (yes/no)"):
            break
        
    print("Thank you for using the ECC App!")



if __name__ == "__main__":
    main()

# ECC App - Elliptic Curve Point Addition Visualizer

This project implements an interactive tool for adding two points on an elliptic curve defined by the equation:

$$
y^2 = x^3 + ax + b
$$

The application verifies that the chosen curve is non-singular, accepts two points on the curve, computes their sum using elliptic curve arithmetic (including handling point doubling), and visualizes the curve along with the points and the connecting line using matplotlib.

## Features

- **Interactive Input**: Prompt-based input for curve parameters and points.
- **Validation**: Checks that the curve is non-singular and that the points lie on the curve.
- **Elliptic Curve Arithmetic**: Supports both point addition and point doubling.
- **Visualization**: Graphical representation of the elliptic curve, input points, and the resulting sum.

## Installation

This project requires Python 3 and the following libraries:

- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

You can install the dependencies using pip:

```bash
pip install numpy matplotlib
```

## Usage

Run the application from the command line:

```bash
python ecc_app.py
```

Follow the on-screen prompts to enter the coefficients for the elliptic curve and the coordinates for points P and Q. The application will compute and display the resulting point, and if applicable, generate a plot of the curve and points.

## Example Run
![image](https://github.com/user-attachments/assets/a790d519-eb80-48a7-bf10-85e314eb3b67)
![Figure_1](https://github.com/user-attachments/assets/64da1f00-7028-4dbe-995b-45187b4b5b54)



## Project Context

This project was created as part of the EEL4347 class (Spring 2025) to demonstrate the implementation and visualization of elliptic curve point addition.

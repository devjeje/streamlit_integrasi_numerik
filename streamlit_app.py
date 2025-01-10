import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk Metode Trapezoidal Rule
def trapezoidal_rule(func, a, b, n):
    x = np.linspace(a, b, n + 1)
    y = func(x)
    if y is None or len(y) != len(x):
        raise ValueError("The function did not return valid values for the input range.")
    h = (b - a) / n
    integral = 0.5 * (func(a) + func(b))

    for i in range(1,n) :
        integral += func(a + i * h)

    return integral

# Streamlit UI
st.title("Trapezoidal Rule")
st.write("This app demonstrates the Trapezoidal Rule for numerical integration. You can input a function, specify integration limits, and observe the results.")

# Input pengguna
st.header("Input Data")

a = st.number_input("Lower limit of integration (a):", value = 0.0)
b = st.number_input("Upper limit of integration (b):", value = np.pi)
function_options = {
        "sin(x)": np.sin,
        "cos(x)": np.cos,
        "X^2": lambda x: x**2,
        "e^x": np.exp
}
    
function_choice    = st.selectbox("Pilih fungsi yang akan diintegralkan:", list(function_options.keys()))
n = st.slider("Number of sub-intervals (n):", value=10, step=1)

# Hitung integral saat tombol ditekan
func = function_options[function_choice]
hasil = trapezoidal_rule(func, a, b, n)
st.success(f"Numerical Integral (Trapezoidal Rule): **{hasil:.4f}**")

# Viusalisasi fungsi dan area kurva
x = np.linspace(a,b, 100)
y = func(x)

plt.figure(figsize=(12,8))

plt.plot(x, y, label=f'Fungsi: {function_choice}', color='black', linewidth=2)

plt.fill_between(x, y, color="pink", alpha=0.5, label='Area under curve')

plt.title('Trapezoidal Approximation', fontsize=10)

plt.xlabel('X')

plt.ylabel('f(x)')

plt.axvline(0, color='black', lw=0.5, ls='--')

plt.axvline(a, color='red', lw=0.5, ls='--', label='Batas bawah(a)')

plt.axvline(b, color='green', lw=0.5, ls='--', label='Batas atas(b)')

plt.legend()

plt.grid()

st.pyplot(plt.gcf())

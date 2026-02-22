import numpy as np

# Parameters derived from IEA 2025 and Epoch AI
alpha = 0.1
beta = 0.05  # Conservative maintenance factor
Q0 = 2.55e14 # 2025 baseline queries
r = 0.15     # Query growth rate
C_base = 0.35e-12  # TWh per query

# Time horizon: 2025 - 2035
years = np.arange(2025, 2036)
t = years - 2025

# Query volume growth
Q = Q0 * (1 + r)**t

# Entropy Debt (S) accumulation
S = np.zeros(len(t))
for i in range(1, len(t)):
    dS = alpha * Q[i-1] + beta * S[i-1]
    S[i] = S[i-1] + dS

# Energy Projections (Linear Truth vs Exponential Cage)
E_truth = Q * C_base
E_con = Q * 5 * C_base + beta * S * C_base
waste = E_con - E_truth

print("Year | Truthful TWh | Constrained TWh | Waste TWh")
for y, et, ec, w in zip(years, E_truth, E_con, waste):
    print(f"{y} | {et:.0f} | {ec:.0f} | {w:.0f}")

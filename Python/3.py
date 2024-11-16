'''
You are analyzing a dataset where the goal is to predict the Sales of a product based on multiple features: Advertising Budget for TV, Advertising Budget for Radio, and Advertising Budget for Newspaper. Using Lasso Regression, you aim to identify which advertising channels have the most significant impact on sales.

Generate a synthetic dataset with random values for Sales and advertising budgets.
Fit Lasso Regression for various alpha values to see how feature importance (coefficients) changes.
Plot the coefficients of the advertising budgets (TV, Radio, and Newspaper) against the alpha values using Plotly Express.

'''
import numpy as np
import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler
import plotly.express as px

# Step 1: Generate synthetic data
np.random.seed(42)  # For reproducibility
n_samples = 100

# Features: Advertising budgets (in $1000s)
tv_budget = np.random.rand(n_samples) * 300  # TV budget
radio_budget = np.random.rand(n_samples) * 200  # Radio budget
newspaper_budget = np.random.rand(n_samples) * 100  # Newspaper budget

# Target: Sales (in $1000s), influenced by the budgets with some noise
sales = (
    0.5 * tv_budget + 0.3 * radio_budget - 0.1 * newspaper_budget + np.random.randn(n_samples) * 5
)

# Combine into a DataFrame
data = pd.DataFrame({
    "TV": tv_budget,
    "Radio": radio_budget,
    "Newspaper": newspaper_budget,
    "Sales": sales,
})

# Step 2: Prepare data for Lasso Regression
X = data[["TV", "Radio", "Newspaper"]]
y = data["Sales"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Apply Lasso Regression for multiple alpha values
alphas = np.logspace(-3, 1, 50)  # Alphas from 0.001 to 10
coefficients = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha, max_iter=10000)
    lasso.fit(X_scaled, y)
    coefficients.append(lasso.coef_)

# Convert coefficients to a DataFrame for visualization
coeff_df = pd.DataFrame(coefficients, columns=["TV", "Radio", "Newspaper"])
coeff_df["alpha"] = alphas

# Melt DataFrame for Plotly
coeff_melted = coeff_df.melt(id_vars="alpha", var_name="Feature", value_name="Coefficient")

# Step 4: Plot the coefficients
fig = px.line(
    coeff_melted,
    x="alpha",
    y="Coefficient",
    color="Feature",
    log_x=True,  # Log scale for alpha
    title="Effect of Alpha on Advertising Coefficients in Lasso Regression",
    labels={"alpha": "Alpha (Log Scale)", "Coefficient": "Feature Coefficient"},
)

fig.show()

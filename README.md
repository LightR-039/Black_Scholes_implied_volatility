# Black–Scholes Implied Volatility Solver

A Python implementation of the **Black–Scholes option pricing model** used to compute **implied volatility** from observed market option prices. This project demonstrates how mathematical finance theory, numerical methods, and visualization combine to solve a real quantitative trading problem.

---

## 📌 Project Overview

In real financial markets, option prices are observable — but **volatility is not directly visible**.

This project focuses on solving the inverse pricing problem:

> **Given a market option price, what volatility is implied by the Black–Scholes model?**

This quantity, called **implied volatility**, is one of the most important metrics in options markets. It reflects market expectations of uncertainty and risk.

The project builds a compact pricing engine that:

* Prices European call options with Black–Scholes
* Numerically solves for implied volatility
* Verifies model accuracy
* Visualizes the price–volatility relationship

---

## 🧠 Black–Scholes Model: Mathematical Foundation

The Black–Scholes model assumes that stock prices follow a **geometric Brownian motion**:

```
dS = μS dt + σS dW
```

where:

* S = stock price
* μ = expected return
* σ = volatility
* dW = Brownian motion

Under risk-neutral valuation, the price of a European call option is:

```
C = S N(d1) − K e^(−rT) N(d2)
```

where:

```
d1 = [ln(S/K) + (r + σ²/2)T] / (σ√T)
d2 = d1 − σ√T
```

and:

* N(·) = cumulative normal distribution
* K = strike price
* r = risk-free rate
* T = time to maturity
* σ = volatility

This formula gives option price as a function of volatility:

```
C = f(σ)
```

---

## 🎯 Focus of This Project: Implied Volatility

In practice:

* Market price **C_market** is known
* Volatility **σ** is unknown

We solve:

```
f(σ) − C_market = 0
```

This equation has no closed-form solution for σ.

Therefore, we use **numerical root-finding**.

---

## 🔬 Numerical Method Used

The project implements an iterative solver based on Newton’s method.

The update rule is:

```
σ_new = σ_old − (f(σ_old) − C_market) / Vega
```

where **Vega** measures sensitivity to volatility:

```
Vega = S √T φ(d1)
```

and φ(·) is the normal probability density function.

The algorithm proceeds:

1. Start with an initial volatility guess
2. Compute model price and Vega
3. Update volatility estimate
4. Repeat until convergence
   
---

## 🏗️ Project Structure

```
Black_Scholes_implied_volatility/
│
├── src/
│   ├── black_scholes.py     
│   ├── solvers.py           
│   ├── validation.py        
│   └── visualization.py   
│
├── implied_vol_demo.ipynb  
├── environment.yml         
├── README.md
└── LICENSE
```

---

## 📈 Example Demonstration

The demo notebook evaluates a realistic market scenario:

* Stock price: 100
* Strike price: 100
* Time to maturity: 1 year
* Risk-free rate: 2%
* Observed option price: 10

```
Calculated Implied volatility: 0.2277230315705129
```

### Interpretation of the Results

The computed implied volatility of **22.77%** means that the market is pricing the option as if the underlying asset is expected to fluctuate by roughly 22.77% per year.

The solver converges in only **3 iterations**, showing that Newton’s method efficiently finds the root of the pricing equation. The model price matches the observed market price almost exactly (the tiny difference is due to floating-point precision), confirming that the algorithm successfully solved:

```
Black–Scholes price ≈ Market price
```

This implied volatility has direct practical meaning for traders:

* If a trader believes future volatility will be **higher than 22.77%**, the option may be undervalued → buying options could be attractive.
* If the trader expects **lower volatility**, the option may be overpriced → selling or writing options may be preferable.

Implied volatility therefore acts as a bridge between mathematical models and trading decisions. It helps professionals:

* Compare options across markets
* Assess market expectations of risk
* Identify potential mispricing
* Guide hedging and speculative strategies

---

## ⚙️ Setup

Clone the repository and create the environment:

```
conda env create -f environment.yml
conda activate <env_name>
```

Run the demo notebook:

```
jupyter notebook
```

Open:

```
implied_vol_demo.ipynb
```

---

## 📜 License

Released under the MIT License.

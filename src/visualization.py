import numpy as np
import matplotlib.pyplot as plt

from .black_scholes import (
    black_scholes_call,
    black_scholes_put,
)
from .solvers import implied_volatility


def plot_price_vs_volatility(
    S,
    K,
    T,
    r,
    market_price,
    option_type="call",
):
    sigmas = np.linspace(0.001, 1.0, 100)
    prices = []

    for sigma in sigmas:
        if option_type == "call":
            price = black_scholes_call(S, K, T, r, sigma)
        else:
            price = black_scholes_put(S, K, T, r, sigma)

        prices.append(price)

    iv, _, success = implied_volatility(
        market_price, S, K, T, r, option_type
    )

    plt.figure()
    plt.plot(sigmas, prices, label="Model Price")
    plt.axhline(market_price, linestyle="--", label="Market Price")

    if success:
        plt.axvline(iv, linestyle="--", label=f"IV = {iv:.4f}")

    plt.xlabel("Volatility")
    plt.ylabel("Option Price")
    plt.title("Option Price vs Volatility")
    plt.legend()
    plt.grid(True)
    plt.show()

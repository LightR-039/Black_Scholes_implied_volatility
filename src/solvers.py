from .black_scholes import (
    black_scholes_call,
    black_scholes_put,
    black_scholes_vega,
)
from .validation import is_valid_option_price


def implied_volatility_bisection(
    market_price,
    S,
    K,
    T,
    r,
    option_type="call",
    tol=1e-6,
    max_iter=100,
):
    sigma_low = 0.001
    sigma_high = 3.0

    for i in range(max_iter):
        sigma_mid = 0.5 * (sigma_low + sigma_high)

        if option_type == "call":
            price = black_scholes_call(S, K, T, r, sigma_mid)
        else:
            price = black_scholes_put(S, K, T, r, sigma_mid)

        diff = price - market_price

        if abs(diff) < tol:
            return sigma_mid, i + 1, True

        if diff > 0:
            sigma_high = sigma_mid
        else:
            sigma_low = sigma_mid

    return sigma_mid, max_iter, False


def implied_volatility_newton(
    market_price,
    S,
    K,
    T,
    r,
    option_type="call",
    initial_sigma=0.2,
    tol=1e-6,
    max_iter=100,
):
    sigma = initial_sigma

    for i in range(max_iter):
        if option_type == "call":
            price = black_scholes_call(S, K, T, r, sigma)
        else:
            price = black_scholes_put(S, K, T, r, sigma)

        diff = price - market_price

        if abs(diff) < tol:
            return sigma, i + 1, True

        vega = black_scholes_vega(S, K, T, r, sigma)

        if vega < 1e-8:
            return sigma, i + 1, False

        sigma = sigma - diff / vega
        sigma = max(0.001, min(sigma, 3.0))

    return sigma, max_iter, False


def implied_volatility(
    market_price,
    S,
    K,
    T,
    r,
    option_type="call",
):
    if not is_valid_option_price(market_price, S, K, T, r, option_type):
        return None, 0, False

    sigma, iters, success = implied_volatility_newton(
        market_price, S, K, T, r, option_type
    )

    if success:
        return sigma, iters, True

    return implied_volatility_bisection(
        market_price, S, K, T, r, option_type
    )

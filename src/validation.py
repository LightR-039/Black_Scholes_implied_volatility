import numpy as np


def is_valid_option_price(market_price, S, K, T, r, option_type="call"):
    discount = np.exp(-r * T)

    if option_type == "call":
        intrinsic = max(S - K * discount, 0)
        upper_bound = S
    else:
        intrinsic = max(K * discount - S, 0)
        upper_bound = K * discount

    return intrinsic <= market_price <= upper_bound

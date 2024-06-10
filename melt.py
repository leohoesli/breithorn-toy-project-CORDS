import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def synthetic_P(t):
    return np.full_like(t, 8e-3)

def synthetic_T(t):
    return -10*np.cos(2*np.pi/364 * t) - 8*np.cos(2*np.pi* t) + 5


def melt(T, melt_factor):

    if T >= 0:
        return T * melt_factor
    else:
        return 0.0

def accumulate(T, P, T_threshold):
    
    if T <= T_threshold:
        return P
    else:
        return 0.0
    
def lapse(T, dz, lapse_rate):
    
    return lapse_rate * dz + T

def net_balance_fn(dt, Ts, Ps, melt_factor, T_threshold):
    """
    Integrate the balance rate (this is at a point) over time for given temperature and precipitation arrays to get the "net balance".

    Args:
        dt: The time step.
        Ts: Array of temperatures.
        Ps: Array of precipitations.
        melt_factor: The factor to compute melt amount.
        T_threshold: The temperature threshold for accumulation.

    Returns:
        net balance (this is at a point)
    """
    assert len(Ts) == len(Ps)
    total = 0.0
    for T, P in zip(Ts, Ps):
        balance_rate = -melt(T, melt_factor) + accumulate(T, P, T_threshold)
        total += balance_rate * dt
    return total


def glacier_net_balance_fn(zs, dt, Ts, Ps, melt_factor, T_threshold, lapse_rate):
    """
    Calculate:
    - the glacier net balance (integration of balance rate over time and space)
    - the net balance at each point (integration of balance rate over time)

    Args:
        zs: Array of elevations (with the weather station as datum)
        dt: The time step.
        Ts: Array of temperatures.
        Ps: Array of precipitations.
        melt_factor: The factor to compute melt amount.
        T_threshold: The temperature threshold for accumulation.
        lapse_rate: The lapse rate (temperature change per unit elevation change).

    Returns:
        the glacier net balance [m]
        net balance at all points [m]
    """
    glacier_net_balance = 0.0
    net_balance = np.zeros(len(zs))
    for i, z in enumerate(zs):
        TT = [lapse(T, z, lapse_rate) for T in Ts]
        net_balance[i] = net_balance_fn(dt, TT, Ps, melt_factor, T_threshold)
        glacier_net_balance += net_balance[i]
    return glacier_net_balance / len(zs), net_balance


# Constants

melt_factor = 0.005  # m/d/°C
lapse_rate = -0.6/100
melt_factor = 0.005
T_threshold = 4
dt = 1 / 24
t = np.arange(0, 365 + dt, dt)




# Test cases
def test_lapsed_temperature():
    assert lapse(5, 2500, -0.009) == 0.5
    assert lapse(10, 1000, -0.006) == 4.0

def test_glacier_melt():
    assert melt(5, 0.005) == 0.025
    assert melt(-5, 0.005) == 0.0

def test_glacier_accumulation():
    assert accumulate(-5, 0, 0.5) == 0.5
    assert accumulate(4, 4, 10) == 10
    assert accumulate(0, 0, 0.5) == 0.5

# Run tests
# test_lapsed_temperature()
# test_glacier_melt()
# test_glacier_accumulation()

# print("All tests passed.")

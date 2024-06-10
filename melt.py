import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def precip_synthetic(t):
    return 8e-3

def temperature_synthetic(t):
    return -10*np.cos(2*np.pi/364 * t) - 8*np.cos(2*np.pi* t) + 5



def glacier_melt(temperature, melt_factor):

    if temperature >= 0:
        return temperature * melt_factor
    else:
        return 0.0

def  glacier_accumulation(temperature, t_threshold, precip):
    
    if temperature <= t_threshold:
        return precip
    else:
        return 0.0
    
def lapsed_temperature(temperature_s, elevation, lapse_rate):
    
    delta_h = elevation - elevation_s
    return lapse_rate * delta_h + temperature_s


# Example usage
temperature_s = 5    # °C, temperature at weather station
elevation_s = 2000   # m, elevation of the weather station
melt_factor = 0.005  # m/d/°C
precip = 0.5         # m
lapse_rate = -0.009  # °C/m
elevation = 2500     # example elevation
t_threshold = 0      # °C, temperature threshold
temperature = lapsed_temperature(temperature_s, elevation, lapse_rate)
melt = glacier_melt(temperature, melt_factor)
accumulation = glacier_accumulation(temperature, t_threshold, precip)
print(f"Glacier melt: {melt} m/d, Glacier accumulation: {accumulation}")

# Test cases
def test_lapsed_temperature():
    assert lapsed_temperature(5, 2500, -0.009) == 0.5
    assert lapsed_temperature(10, 1000, -0.006) == 4.0

def test_glacier_melt():
    assert glacier_melt(5, 0.005) == 0.025
    assert glacier_melt(-5, 0.005) == 0.0

def test_glacier_accumulation():
    assert glacier_accumulation(-5, 0, 0.5) == 0.5
    assert glacier_accumulation(4, 4, 10) == 10
    assert glacier_accumulation(0, 0, 0.5) == 0.5

# Run tests
# test_lapsed_temperature()
test_glacier_melt()
test_glacier_accumulation()

print("All tests passed.")
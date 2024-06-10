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
temperature = lapsed_temperature(temperature_s, elevation, lapse_rate)
melt = glacier_melt(temperature, melt_factor)
accumulation = glacier_accumulation(temperature, 0, precip)
print(f"Glacier melt: {melt} m/d, Glacier accumulation: {accumulation}")


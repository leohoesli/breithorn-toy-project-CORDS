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
    
def lapsed_temperature(temperature_s, delta_h, lapse_rate):
    
    return lapse_rate * delta_h + temperature_s


# Example usage
temperature_s = 2.5  # Example temperature in degrees Celsius
melt_factor = 0.5  # Example melt factor (unit of melt per degree Celsius)
precip = 0.5
lapse_rate = -0.009  # °C/m
delta_h = 200
temperature = lapsed_temperature(temperature_s, delta_h, lapse_rate)
melt = glacier_melt(temperature, melt_factor)
accumulation = glacier_accumulation(temperature, 0, precip)
print(f"Glacier melt: {melt} units, Glacier accumulation: {accumulation}")


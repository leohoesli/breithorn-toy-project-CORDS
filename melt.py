def glacier_melt(temperature, melt_factor):

    if temperature >= 0:
        return temperature * melt_factor
    else:
        return 0.0

# Example usage
temperature = 2.5  # Example temperature in degrees Celsius
melt_factor = 0.5  # Example melt factor (unit of melt per degree Celsius)
melt = glacier_melt(temperature, melt_factor)
print(f"Glacier melt: {melt} units")


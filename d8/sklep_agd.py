from d8.male_agd import Device

zelazko = Device("żelazko", 2700)

print(zelazko)

zelazko.power_consumption()
print(zelazko.yearly_consumption_price(12))
zelazko.turn_on()
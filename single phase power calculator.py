# single_phase_power_calculator.py

import math

print("======================================")
print("   SINGLE PHASE POWER CALCULATOR")
print("======================================")

print("\n1. Calculate Power")
print("2. Calculate Current")
print("3. Calculate Power Factor")

choice = int(input("\nEnter your choice (1-3): "))

if choice == 1:
    voltage = float(input("Enter Voltage (V): "))
    current = float(input("Enter Current (A): "))
    pf = float(input("Enter Power Factor (0-1): "))

    apparent_power = voltage * current
    real_power = voltage * current * pf
    reactive_power = math.sqrt(apparent_power**2 - real_power**2)

    print("\n----- RESULTS -----")
    print(f"Apparent Power = {apparent_power:.2f} VA")
    print(f"Real Power     = {real_power:.2f} W")
    print(f"Reactive Power = {reactive_power:.2f} VAR")

elif choice == 2:
    voltage = float(input("Enter Voltage (V): "))
    power = float(input("Enter Real Power (W): "))
    pf = float(input("Enter Power Factor (0-1): "))

    current = power / (voltage * pf)

    print("\n----- RESULTS -----")
    print(f"Current = {current:.2f} A")

elif choice == 3:
    power = float(input("Enter Real Power (W): "))
    voltage = float(input("Enter Voltage (V): "))
    current = float(input("Enter Current (A): "))

    pf = power / (voltage * current)

    print("\n----- RESULTS -----")
    print(f"Power Factor = {pf:.3f}")

else:
    print("Invalid choice!")

print("\nCalculation completed.")

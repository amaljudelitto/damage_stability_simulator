import json
import matplotlib.pyplot as plt
from hydrostatics import calc_GZ, calc_BM

with open("example_input.json", "r") as f:
    ship = json.load(f)

heel_angles = list(range(0, 61))  # 0° to 60°

# Inputs
B = ship["beam"]
T = ship["draft"]
KB = 0.53 * T
KG_intact = ship["KG_intact"]
KG_damaged = ship["KG_damaged"]
V = ship["volume"]
I = ship["waterplane_moi"]

BM = calc_BM(I, V)

GZ_intact = [calc_GZ(B, T, angle, KB, KG_intact, BM) for angle in heel_angles]
GZ_damaged = [calc_GZ(B, T, angle, KB, KG_damaged, BM) for angle in heel_angles]

plt.plot(heel_angles, GZ_intact, label="Intact")
plt.plot(heel_angles, GZ_damaged, label="Damaged", linestyle="--")
plt.xlabel("Heel Angle (°)")
plt.ylabel("Righting Arm (GZ) [m]")
plt.title("GZ Curve (Intact vs Damaged)")
plt.legend()
plt.grid(True)
plt.show()

import math

def calc_GZ(B, T, heel_angle_deg, KB, KG, BM):
    heel_rad = math.radians(heel_angle_deg)
    GM = KB + BM - KG
    GZ = GM * math.sin(heel_rad)
    return max(GZ, 0)

def calc_BM(I, V):
    return I / V

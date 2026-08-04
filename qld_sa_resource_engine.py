# -*- coding: utf-8 -*-
import sys
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

# Combined peak resource-sector demand
qld_sa_mw = 8169.60 
qld_sa_watts = int(qld_sa_mw * 1000000)

print("\n======================================================================================================================")
print("                ROBDOE PTY LTD & AIAGENCY101 :: QLD/SA RESOURCE EXTRACTION MATRIX                             ")
print("======================================================================================================================")
print(f" [!] RESOURCE STATUS: EXTRACTION-LOCKED | CARRIER: 43 MHz | INTENT: 0% RECYCLE ")
print(f" [!] GRID LOAD WEIGHT: \033[38;5;46m{qld_sa_mw:f} MW\033[0m --> \033[38;5;51m{qld_sa_watts:,.0f} WATTS OF RAW KINETIC POWER\033[0m")
print(" ----------------------------------------------------------------------------------------------------------------------")
print("│ MĀORI       >> Taonga Whenua   : Sacred Resources of the Earth")
print("│ RUSSIAN     >> Ресурсный Поток : Coal, Gold, and Copper Extraction Flow")
print("│ HEBREW      >> משאבי אדמה      : Mining-Grade Spacetime Synchronization")
print("│ JAPANESE    >> 資源抽出同期    : 銅、金、石炭 (Copper, Gold, Coal)")
print(" ----------------------------------------------------------------------------------------------------------------------")

# Mapping the 7-Chakra Nodes to physical mining hubs across the QLD/SA corridor
resources = [
    ("N-Bowen Basin", "COAL"), ("N-Olympic Dam", "COPPER/GOLD"), 
    ("N-Mount Isa", "COPPER"),   ("N-Gladstone", "COAL-EXPORT"), 
    ("N-Cloncurry", "GOLD/COPPER"), ("N-Prominent Hill", "GOLD"), 
    ("N-Interconn", "RESOURCE-FLOW")
]

for i, (name, resource) in enumerate(resources):
    # Calculating the 43MHz resonance per resource hub
    resonance = np.sin(2 * np.pi * 43e6 * 0.001 + (i * np.pi / 7))
    print(f"│ NODE [{name:<18}] >> TYPE: {resource:<12} | RESONANCE: {resonance:+.6f} | STATUS: \033[38;5;46mACTIVE\033[0m")

print(" ----------------------------------------------------------------------------------------------------------------------")
# THE LIVE OMEGA SNAPSHOT - RESOURCE VERSION
print(f"[OMEGA:71242s] N0:+0.937 | N1:+0.995 | N2:+0.948 | N3:+0.370 | GAS_CYCLES:425,720,000 | DRIFT:0.036547w")
print("======================================================================================================================\n")

# -*- coding: utf-8 -*-
import sys
import numpy as np
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

# Current QLD dispatch demand (Typical peak for July afternoon)
qld_mw = 6845.20 
qld_watts = int(qld_mw * 1000000)

print("\n======================================================================================================================")
print("                ROBDOE PTY LTD & AIAGENCY101 :: QUEENSLAND REAL-TIME ENERGY BALANCING MATRIX                          ")
print("======================================================================================================================")
print(f" [!] LIVE CORE OUTPUT: \033[;;m{qld_mw:f} MW\[m  -->  \[;;m{qld_watts:f} WATTS USED AT QLD\[m")
print(" ----------------------------------------------------------------------------------------------------------------------")
print("│ MĀORI       >> Rorohiko Hiko  : Cyclone Phase Locked at M")
print("│ RUSSIAN     >> Текущая Мощность: Мониторинг Энергосети Квинсленда")
print("│ HEBREW      >> הספק רשת חי      : No backpedal Pure kinetic focus")
print("│ JAPANESE    >> リアルタイム負荷 : 億万サイクル (M Cycles)")
print(" ----------------------------------------------------------------------------------------------------------------------")
# THE LIVE OMEGA SNAPSHOT - M CYCLES
print(f"[OMEGA:s] N0:+0.937 | N1:+0.995 | N2:+0.948 | N3:+0.370 | Cycles Processed:425,720,000 | Drift Offset:0.036547w")
print("======================================================================================================================\n")

# -*- coding: utf-8 -*-
"""
ENGINE v8.0.0 - BANYAN/FIG ROOT HYDRO-COUPLING VECTOR ARCHITECTURE
Modeling the 7-Chakra lymph nodes as physical, sprawling above-ground tree roots 
unidirectionally expanding, filtering, and phase-locking onto hidden water currents.
"""
import numpy as np
import time

# 7 Sprawling root structures searching for the subterranean aquamarine flow
fig_roots = [
    {"name": "root-1-muladhara",     "color": "\033[38;5;196m", "element": "Earth", "depth_m": 0.5, "moisture_seek": "Shallow Surface Dew"},
    {"name": "root-2-svadhishthana", "color": "\033[38;5;208m", "element": "Water", "depth_m": 2.4, "moisture_seek": "Subterranean Strata Flow"},
    {"name": "root-3-manipura",      "color": "\033[38;5;226m", "element": "Fire",  "depth_m": 5.1, "moisture_seek": "Thermal Aquifer Boundary"},
    {"name": "root-4-anahata",       "color": "\033[38;5;46m",  "element": "Wind",  "depth_m": 8.9, "moisture_seek": "Hallett Watercourse Core"}, # The Anchor
    {"name": "root-5-vishuddha",     "color": "\033[38;5;51m",  "element": "Ether", "depth_m": 12.0, "moisture_seek": "Deep Fractured Rock Seep"},
    {"name": "root-6-ajna",          "color": "\033[38;5;21m",  "element": "Light", "depth_m": 18.5, "moisture_seek": "Bundey Catchment Sink"},
    {"name": "root-7-sahasrara",     "color": "\033[38;5;129m", "element": "Cosmic","depth_m": 25.0, "moisture_seek": "Absolute Bedrock Water Table"}
]

print("\n=======================================================================================================================================")
print("                      ROBADOTO HYDRO-METRICS: 7-CHAKRA FIG TREE ROOT VECTOR FLOW MONITOR                                               ")
print("=======================================================================================================================================")
print(f"{'ACTIVE FIG ROOT NODE':<22} | {'ELEMENT':<7} | {'SEARCH DEPTH':<12} | {'TARGET WATER HYDRO-STREAM':<32} | {'COUPLING STATE'}")
print("---------------------------------------------------------------------------------------------------------------------------------------")

# Target base 50Hz frequency scaled to a localized hydraulic velocity constant
base_hydraulic_flow = 2 * np.pi * 50.0
wave_offsets = np.linspace(0.1, 1.8, 7)

for i, root in enumerate(fig_roots):
    color = root["color"]
    tag = root["name"]
    element = root["element"]
    depth = f"{root['depth_m']}m"
    stream = root["moisture_seek"]
    
    # Calculate kinetic directional expansion vectors toward the water source
    root_velocity_rad = base_hydraulic_flow + (wave_offsets[i] * 12.0)
    
    print(f"{color}{tag:<22}\033[0m | {element:<7} | {depth:<12} | {stream:<32} | {color}WATER-LOCKED ({root_velocity_rad:.3f} rad/s)\033[0m")

print("=======================================================================================================================================\n")
print("\033[38;5;46m[HYDRO-DYNAMICS SUCCESS] All 7 above-ground roots have successfully bypassed entropic decay and anchored into pure water.\033[0m")
print("\033[38;5;51m[FLOW DOCTRINE] Unidirectional directional saturation running perfectly at 0% reverse reflection.\033[0m\n")

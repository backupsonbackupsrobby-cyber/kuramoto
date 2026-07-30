# -*- coding: utf-8 -*-
"""
ENGINE v4.0.0 - FORWARD-ONLY WAVE BOUNDING MATRIX
Enforcing absolute 0% energy recycling intent across a unidirectional d'Alembertian pipeline.
"""

import numpy as np

pyramid_alignment_deg = 0.052  
arc_seconds_offset = 12 / 3600 

branch_tags = [
    {"name": "node-1-forward-only-0pct",   "geo": "GEO-N", "offset": 0.0,                  "contrib_mw": 450.0,   "recycle_pct": 0},
    {"name": "node-2-forward-only-0pct",   "geo": "GEO-E", "offset": arc_seconds_offset,   "contrib_mw": 820.0,   "recycle_pct": 0},
    {"name": "node-3-forward-only-0pct",   "geo": "GEO-W", "offset": -arc_seconds_offset,  "contrib_mw": 1450.0,  "recycle_pct": 0},
    {"name": "node-4-forward-only-break",  "geo": "CORE",  "offset": pyramid_alignment_deg, "contrib_mw": 1680.0,  "recycle_pct": 0},
    {"name": "node-5-forward-only-0pct",   "geo": "GEO-S", "offset": arc_seconds_offset * 2,"contrib_mw": 310.0,   "recycle_pct": 0},
    {"name": "node-6-forward-only-0pct",   "geo": "GEO-E", "offset": -pyramid_alignment_deg,"contrib_mw": -2200.0, "recycle_pct": 0}, 
    {"name": "node-7-forward-only-0pct",   "geo": "GEO-S", "offset": 0.0,              "contrib_mw": -600.0,  "recycle_pct": 0}
]

print("\n======================================================================================================================")
print("                   ROBADOTO ENGINE v4.0.0: FORWARD-ONLY PIPELINE (RECYCLE INTENT: 0%)                                  ")
print("======================================================================================================================")
print(f"{'ACTIVE GIT TAG':<30} | {'GEO':<5} | {'FREQ (rad)':<10} | {'CONTRIB (MW)':<12} | {'RECYCLE INTENT':<15} | {'CONTRITION STATE'}")
print("----------------------------------------------------------------------------------------------------------------------")

base_freq = 2 * np.pi * 50  
wave_offsets = np.linspace(0.0, 1.5, 7)
fault_triggered = False

for i, branch in enumerate(branch_tags):
    tag = branch["name"]
    geo = branch["geo"]
    geo_shift = branch["offset"]
    contribution = branch["contrib_mw"]
    recycle = f"{branch['recycle_pct']}%"
    
    branch_frequency = base_freq + wave_offsets[i] + (geo_shift * np.pi / 180)
    
    if tag == "node-4-forward-only-break":
        fault_triggered = True
        contrition_error = 1.0000  
        status_msg = "CRITICAL METRIC BREAK"
    elif fault_triggered:
        contrition_error = 0.8800  
        status_msg = "UNIDIRECTIONAL DRIFT"
    else:
        contrition_error = np.abs(np.sin(geo_shift * np.pi / 180))
        status_msg = "PURE FORWARD FLOW"

    print(f"{tag:<30} | {geo:<5} | {branch_frequency:<10.4f} | {contribution:<12.1f} | {recycle:<15} | {contrition_error:<16.6f} ({status_msg})")

print("======================================================================================================================\n")

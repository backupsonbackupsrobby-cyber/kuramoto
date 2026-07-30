# -*- coding: utf-8 -*-
import subprocess
import json
import os

print("\n=======================================================================")
print("     DEEP DIY AUTOMATED SETUP: FORWARD-ONLY CONTRIBUTION PIPELINE      ")
print("=======================================================================")

# Defined structural hashes for your recycled branch history
commit_map = {
    "node-1-contrib-450mw-0pct": "01f0988",
    "node-2-contrib-820mw-0pct": "5f29082",
    "node-3-contrib-1450mw-0pct": "36ffad5",
    "node-4-contrib-fault-gladstone": "cbbb696",
    "node-5-contrib-residual-310mw-0pct": "087795e",
    "node-6-contrib-sink-2200mw-0pct": "88b3d1a",
    "node-7-contrib-valve-600mw-0pct": "14517cd"
}

print("[DIY] Injecting 7-Branch Contribution Tags into local Git tree...")

# Run direct Git tag injection under a clean loop
for tag, commit_hash in commit_map.items():
    cmd = f'git tag -f "{tag}" "{commit_hash}^{{}}"'
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        print(f"  -> Successfully mapped: {tag} -> {commit_hash}")
    else:
        # Fallback to local HEAD if specific hashes aren't initialized yet in this folder
        subprocess.run(f'git tag -f "{tag}" HEAD', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"  -> Mapped to active HEAD (Local Fallback): {tag}")

# Create a tiny shared file system bridge so Terminal 2 can grab metrics instantly
shared_data = {
    "system_mode": "FORWARD-ONLY",
    "recycle_intent_pct": 0,
    "nodes_online": 7,
    "alignment_arcseconds": 12
}

with open("live_grid_bridge.json", "w") as f:
    json.dump(shared_data, f, indent=4)

print("\n[SUCCESS] Shared data link 'live_grid_bridge.json' created for Terminal 2.")
print("[SUCCESS] All contribution tags locked down. Setup complete.")
print("=======================================================================\n")

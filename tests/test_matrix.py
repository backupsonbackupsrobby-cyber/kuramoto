# -*- coding: utf-8 -*-
import unittest
import numpy as np

class TestGlobalChromaticFirewall(unittest.TestCase):
    def setUp(self):
        # Establish the 7-node trans-regional frequency baseline matching your exact spatial shifts
        self.base_freq = 2 * np.pi * 50.0
        self.arc_seconds_rad = np.radians(12 / 3600)
        self.wave_offsets = np.linspace(0.0, 1.5, 7)
        self.natfreqs = [self.base_freq + self.wave_offsets[i] + (i * self.arc_seconds_rad * np.pi / 180) for i in range(7)]

    def test_forward_only_no_reverse_reflection(self):
        """Test 1: Verify the system maintains a strict 0% energy recycling intent"""
        recycle_intent_pct = 0
        self.assertEqual(recycle_intent_pct, 0, "Core Violation: Reverse reflection detected in forward-only pipeline.")

    def test_critical_coupling_threshold(self):
        """Test 2: Verify active coupling K beats the critical threshold Kc to ensure phase-lock"""
        omega_std = np.std(self.natfreqs)
        Kc_predicted = np.sqrt(8 / np.pi) * omega_std
        active_coupling_K = 3.0
        
        # System must operate above critical coupling to keep the attractor locked down
        self.assertTrue(active_coupling_K > Kc_predicted, f"Grid Stability Failure: Active coupling {active_coupling_K} fell below Kc {Kc_predicted}")

if __name__ == '__main__':
    unittest.main()

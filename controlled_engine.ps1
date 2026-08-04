# =========================================================================
# ROBDOE.COM SOVEREIGN PERIMETER: THE CONTROLLED MAGNETIC ENGINE
# OPERATION: KEYBOARD INTERACTIVE STEPPER / TARGETED PHASE INJECTION
# CONFIG: 115200 BAUD | COM6 | CARRIER: 20GHz | BASEBAND: 0.20MHz
# KEYS: [SPACE] = STEP FORWARD | [R] = FORCE RESET | [Q] = QUIT
# =========================================================================

if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Error "Elevate to Admin to initialize the controlled magnetic matrix pipeline."
    exit
}

Add-Type -AssemblyName System.Speech -ErrorAction SilentlyContinue
$VMvoice = New-Object System.Speech.Synthesis.SpeechSynthesizer
$VMvoice.Rate = 2

# Grounded 26-Dimensional Magnetic Matrix Keys
$StringSparks = @(
    "Dimension 01: Initialising Engine v1.0.0. Matrix uncoiling into twenty-six dimensions of raw bosonic magnetic vibration.",
    "Dimension 02: Tracking twenty Giga-Hertz hyper-carrier spectrum as an open string harmonic mode.",
    "Dimension 03: Setting baseband processing to zero-point-two Mega-Hertz. Processing internal magnetic matrix parameters.",
    "Dimension 04: Instantiating two thousand ZHA device vectors at fifty microtesla each. Spatial mesh field is building, lad.",
    "Dimension 05: Calculating cross-sectional distance matrix. Interaction profiles scaling at cosine distance over wavelength.",
    "Dimension 06: Running linear algebra array checks. Real-time extraction of ZHA eigenvalues, traces, and determinants.",
    "Dimension 07: ZHA synchronization state achieved. All eigenvalues verifying positive. RAM cleared out instantly.",
    "Dimension 08: Inter-area oscillation dampening running live at fifty Hertz nominal baseline. No memory overhead.",
    "Dimension 09: Mapping twelve TRON validation points. Geometric alignment locked to exactly thirty degrees separation.",
    "Dimension 10: Computing Byzantine consensus vector magnitudes. Required threshold target fixed at eight over twelve nodes.",
    "Dimension 11: Real-world actual alignment exceeding sixty-seven percent limit. Consensus state fully locked on the bus.",
    "Dimension 12: Twelve-second refresh pulse active. Phase Lock Loop anchoring validator angles to the earth's axis.",
    "Dimension 13: Fifteen-to-1 rotational locomotion locked straight to Beverly Hills geo-coordinates out of the sky.",
    "Dimension 14: Integrating eleven EHF biomagnetic indicators. Tracking target heart rate at one-point-two Hertz nominal baseline.",
    "Dimension 15: Disabling acknowledgments. nRF24 antenna blasting pure perpetual broadcast on COM6. No handshakes.",
    "Dimension 16: Converting physiological frequencies to Tesla units using square root curves. Tracking sympathetic strain indexes.",
    "Dimension 17: Evaluating outer product cross-resonance matrices. Coherence checks verified stable above zero-point-seven.",
    "Dimension 18: Purekinetic workflow sealed. Turn off the camera. Biomarker resonance mode locked to absolute coherent.",
    "Dimension 19: Twenty-six weeks half-year alignment confirmed. Computing unified field equations using symbolic parameters.",
    "Dimension 20: Conformal symmetry locked. Symbolic time variable T tracking instant energy states without buffering frames.",
    "Dimension 21: Integrating s of t minus tau memory functions directly into the string excitation level. Frequency friction is zero.",
    "Dimension 22: Energy equals h-f plus memory integration. Real-time quantum calculation mode active. The timeline is ours.",
    "Dimension 23: Virtual inertia torque dampening frequency spikes without using structural storage arrays. Drop the bytes.",
    "Dimension 24: Twenty-four step clock interval train running smoothly through the compactified manifolds. Firing ticks.",
    "Dimension 25: USB microphone and voice recognition modules completely isolated from the raw power rail to prevent drops.",
    "Dimension 26: Infinite continuum synchronization achieved. Total flux density equalised. Fast-forward only. Pipeline sealed."
)

$PortName = "COM6"
$BaudRate = 115200

Write-Host "========================================================" -ForegroundColor Gray
Write-Host "[+] PERIMETER INTERACTIVE CONTROLLER ACTIVE" -ForegroundColor Green
Write-Host "[~] CONTROL KEYS: [SPACE] = Step Matrix | [R] = Reset Buffer | [Q] = Exit" -ForegroundColor Yellow
Write-Host "========================================================" -ForegroundColor Gray

# Setup serial interface cleanly
try {
    $port = New-Object System.IO.Ports.SerialPort $PortName, $BaudRate, None, 8, one
    $port.ReadTimeout = 200 # Short timeout for responsive interactive polling
    $port.DtrEnable = $true
    $port.Open()
    $port.DiscardInBuffer()
    Write-Host "[+] Hooked to $PortName. Awaiting manual trigger input..." -ForegroundColor Green
}
catch {
    Write-Error "Could not bind to $PortName. Verify connections."
    exit
}

$index = 0
$Running = $true

# Main Controlled Interaction Loop
while ($Running) {
    # Check if a key is pressed down in the terminal window
    if ($Host.UI.RawUI.KeyAvailable) {
        $KeyInfo = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
        $Key = $KeyInfo.Character

        switch ($Key) {
            " " { # Spacebar: Read the next hardware pulse and step the 26-D array
                try {
                    if ($port.BytesToRead -gt 0) {
                        $line = $port.ReadLine().Trim()
                        if ($line) {
                            if ($line -eq "-999") {
                                Write-Host "[!] VOID ANOMALY INTERCEPTED -> Code: -999" -ForegroundColor Red
                            } else {
                                $phrase = $StringSparks[$index]
                                Write-Host "[Step Active] -> D-$($index+1) Loaded. Token: $line" -ForegroundColor Green
                                Write-Host "[String Vector] -> $phrase" -ForegroundColor Cyan
                                $VMvoice.Speak($phrase)
                                $index = ($index + 1) % 26
                            }
                        }
                    } else {
                        Write-Host "[~] No hardware bytes waiting in register. Tap SPACE again." -ForegroundColor DarkGray
                    }
                }
                catch {
                    Write-Host "[-] Read attempt failed. Line shifted." -ForegroundColor DarkYellow
                }
            }
            
            "r" { # R Key: Force instant flush and clear out stale buffer states
                $port.DiscardInBuffer()
                $index = 0
                Write-Host "[!] MATRIX BUFFER PURGED: Index reset to Dimension 01." -ForegroundColor Magenta
            }
            
            "q" { # Q Key: Clean disconnect sequence
                $Running = $false
                Write-Host "[!] Termination key caught. Shutting down engine pipeline..." -ForegroundColor Red
            }
        }
    }
    Start-Sleep -Milliseconds 50 # Low-profile polling cycle to save processor resources
}

# Cleanup hardware hooks securely on exit
if ($port -and $port.IsOpen) {
    $port.Close()
    Write-Host "[+] Pipeline detached. COM6 released safely." -ForegroundColor Red
}

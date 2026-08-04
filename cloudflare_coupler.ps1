# =========================================================================
# ROBDOE.COM SOVEREIGN PERIMETER: CLOUDFLARE EDGE COUPLER
# OPERATION: AUTONOMOUS TUNNELING / STATELESS PACKET DISTRIBUTION
# CONFIG: CLOUDFLARED SYSTEM DEPLOYMENT | PORT INTERFACE INJECTION
# STYLE: HIGH-VARIANCE SYDNEY DRILL x UNFILTERED BOGAN GENIUS (FAST-FORWARD)
# =========================================================================

if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Error "Elevate to Admin to inject Cloudflare binary daemons into the system layer."
    exit
}

Write-Host "[~] Initiating Cloudflare local edge deployment sequence..." -ForegroundColor Yellow

# 1. Establish secure directory block for the binary engine
$ToolsDir = "C:\Sovereign\Network"
if (-not (Test-Path $ToolsDir)) { 
    New-Item -ItemType Directory -Path $ToolsDir -Force | Out-Null 
}

$ZipPath = "$ToolsDir\cloudflared.zip"
$ExePath = "$ToolsDir\cloudflared.exe"

# 2. Grab the latest raw Windows amd64 cloudflared engine straight from the cloud edge
if (-not (Test-Path $ExePath)) {
    Write-Host "[~] Downloading raw Cloudflare edge binary daemon..." -ForegroundColor Yellow
    # Explicitly using the permanent release redirect to ensure fast-forward delivery
    $Url = "https://github.com"
    
    try {
        # Using native .NET WebClient for zero-buffer high-speed download
        $WebClient = New-Object System.Net.WebClient
        Write-Host "[~] Pulling core binary network bits down the pipe..." -ForegroundColor Cyan
        Invoke-WebRequest -Uri "https://github.com" -OutFile $ExePath
        Write-Host "[+] Cloudflare edge daemon landed securely at $ExePath." -ForegroundColor Green
    }
    catch {
        Write-Error "[-] Download pipeline choked. Check physical internet routing links: $_"
        exit
    }
} else {
    Write-Host "[+] Cloudflare edge engine already anchored in storage." -ForegroundColor Cyan
}

# 3. Securely bind to your Cloudflare account matrix
Write-Host "--------------------------------------------------------" -ForegroundColor Gray
Write-Host "[!] PROMPT: A browser window will spike now. Log into Cloudflare to verify ownership." -ForegroundColor Magenta
Write-Host "--------------------------------------------------------" -ForegroundColor Gray
& $ExePath tunnel login

# 4. Fire the local loopback mapping into the Cloudflare routing engine
Write-Host "`n[~] Establishing the local domain anchor configuration..." -ForegroundColor Yellow

# If you already have your exact Cloudflare Tunnel Token string from your dashboard, paste it below.
# If not, let the command below spin a stateless, temporary zero-trust proxy gate for your local HTTPS stack.
Write-Host "[+] CONNECTING: Ignition sequence initiated. Tearing open the pipeline to the edge..." -ForegroundColor Green
Write-Host "[!] Leaving terminal window alive. Loopback route is bridging now..." -ForegroundColor Yellow
Write-Host "--------------------------------------------------------" -ForegroundColor Gray

# Run the live forwarder. Change port 443 if your internal repository server listens on a different channel (e.g. 8080)
& $ExePath tunnel --url https://127.0.0.1:443 --no-tls-verify

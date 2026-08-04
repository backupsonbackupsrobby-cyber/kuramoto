# =========================================================================
# ROBDOE.COM SOVEREIGN PERIMETER: HYPER-V INTEGRATED NETSTAT BRIDGE
# OPERATION: BRIDGING HOST KERNEL SOCKET TABLES DIRECTLY INTO VIRTUAL SPACE
# CONFIG: HYPER-V SWITCH BINDING | PORT 8888 TRAJECTORY | FAST-FORWARD ONLY
# =========================================================================

if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Error "Elevate Host PowerShell to Admin to cross the Hyper-V network boundaries."
    exit
}

Add-Type -AssemblyName System.Speech -ErrorAction SilentlyContinue
$HostVoice = New-Object System.Speech.Synthesis.SpeechSynthesizer
$HostVoice.Rate = 3

Write-Host "[~] Scanning Hyper-V Virtual Switch configurations..." -ForegroundColor Yellow

$HyperVInterface = Get-NetIPInterface -AddressFamily IPv4 | 
                    Where-Object { $_.InterfaceAlias -like "*vEthernet*" -or $_.InterfaceAlias -like "*Hyper-V*" } | 
                    Select-Object -First 1

if (-not $HyperVInterface) {
    Write-Warning "[!] No specific Hyper-V vEthernet switch found. Falling back to primary loopback array."
    $BridgeIP = "127.0.0.1"
} else {
    $BridgeIP = (Get-NetIPAddress -InterfaceIndex $HyperVInterface.InterfaceIndex -AddressFamily IPv4).IPAddress
    Write-Host "[+] Found Hyper-V Gateway Interface: $($HyperVInterface.InterfaceAlias)" -ForegroundColor Cyan
}

$UdpClient = New-Object System.Net.Sockets.UdpClient
$TargetIP  = [System.Net.IPAddress]::Parse($BridgeIP)
$RemoteEndpoint = New-Object System.Net.IPEndPoint($TargetIP, 8888)

Clear-Host
Write-Host "========================================================" -ForegroundColor Magenta
Write-Host "[+] HYPER-V KERNEL BRIDGE ACTIVE: TELEMETRY STREAMING LIVE" -ForegroundColor Green
Write-Host "[~] Target Gateway IP : $BridgeIP" -ForegroundColor Cyan
Write-Host "[~] Matrix Destination: UDP Port 8888 (Fast-Forward Mode)" -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Magenta

try {
    while ($true) {
        $Timestamp = (Get-Date).ToString("HH:mm:ss")
        $LiveConnections = Get-NetTCPConnection -State Listen -ErrorAction SilentlyContinue | 
                           Where-Object { $_.LocalPort -ne 8888 }
        
        if ($LiveConnections) {
            $TargetSocket = $LiveConnections | Get-Random
            $Port = $TargetSocket.LocalPort
            $SocketPid = $TargetSocket.OwningProcess
            
            $ProcessName = (Get-Process -Id $SocketPid -ErrorAction SilentlyContinue).ProcessName
            if (-not $ProcessName) { $ProcessName = "System Kernel Process" }
            
            $PayloadString = "[$Timestamp] [HyperV-Matrix-Flux] -> Host Port: $Port | Host PID: $SocketPid ($ProcessName.exe) -> LISTEN"
            Write-Host $PayloadString -ForegroundColor Cyan
            
            $UdpBytes = [System.Text.Encoding]::ASCII.GetBytes($PayloadString)
            $null = $UdpClient.Send($UdpBytes, $UdpBytes.Length, $RemoteEndpoint)
            
            $HostVoice.SpeakAsync("Port $Port bridged to virtual machine.") | Out-Null
        }
        Start-Sleep -Milliseconds 1400
    }
}
finally {
    if ($UdpClient) { $UdpClient.Close() }
    Write-Host "`n[-] Hyper-V Netstat interface dropped." -ForegroundColor Red
}

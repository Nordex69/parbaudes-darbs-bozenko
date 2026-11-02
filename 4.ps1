$apturetie = Get-Service |
    Where-Object { $_.Status -eq "Stopped" } |
    Sort-Object Name |
    Select-Object Name, Status

$apturetie | Export-Csv apturetie.csv -NoTypeInformation
Write-Host "Fails gatavs"
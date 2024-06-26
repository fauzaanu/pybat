param (
    [string]$TaskName,
    [string]$TaskDescription,
    [string]$TaskCommand,
    [string]$TaskArguments,
    [string]$StartTime,
    [string]$RepeatInterval,
    [string]$UserName,
    [string]$Password
)

# Create the task action
$Action = New-ScheduledTaskAction -Execute $TaskCommand -Argument $TaskArguments

# Create the task trigger
$Trigger = New-ScheduledTaskTrigger -Daily -At $StartTime

# Create the task settings
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries

# Create the task
$Task = New-ScheduledTask -Action $Action -Trigger $Trigger -Settings $Settings -Description $TaskDescription

# Register the task
try {
    if ($UserName -and $Password) {
        $SecurePassword = ConvertTo-SecureString $Password -AsPlainText -Force
        $Credential = New-Object System.Management.Automation.PSCredential ($UserName, $SecurePassword)
        Register-ScheduledTask -TaskName $TaskName -InputObject $Task -User $UserName -Password $Password -ErrorAction Stop
    } else {
        Register-ScheduledTask -TaskName $TaskName -InputObject $Task -ErrorAction Stop
    }
    Write-Host "Task '$TaskName' created successfully."

    # Verify the task was created
    $CreatedTask = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
    if ($CreatedTask) {
        Write-Host "Task verification successful. Details:"
        $CreatedTask | Format-List
    } else {
        Write-Host "Task verification failed. The task was not found after creation."
    }
} catch {
    Write-Host "An error occurred while creating the task: $_"
}
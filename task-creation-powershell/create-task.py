import os
import subprocess

from dotenv import load_dotenv


def create_task(task_name, task_description, task_command, task_arguments, start_time, repeat_interval, user_name=None,
                password=None):
    powershell_script = r"task.ps1"  # Update this path
    powershell_command = [
        "powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-File", powershell_script,
        "-TaskName", task_name,
        "-TaskDescription", task_description,
        "-TaskCommand", task_command,
        "-TaskArguments", task_arguments,
        "-StartTime", start_time,
        "-RepeatInterval", repeat_interval
    ]

    if user_name and password:
        powershell_command.extend(["-UserName", user_name, "-Password", password])

    try:
        result = subprocess.run(powershell_command, capture_output=True, text=True, check=True)
        print(result.stdout)

        # Check if the task was created
        check_command = f"powershell.exe Get-ScheduledTask -TaskName '{task_name}' | Format-List"
        check_result = subprocess.run(check_command, capture_output=True, text=True, shell=True)
        print("Task details:")
        print(check_result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        print(f"Error output: {e.stderr}")


# P: Designator for period
# T: Designator for time (separates date and time parts)
# nY: Number of years
# nM: Number of months (or minutes if after T)
# nD: Number of days
# nH: Number of hours
# nM: Number of minutes
# nS: Number of seconds

if __name__ == "__main__":
    load_dotenv()
    create_task(
        task_name="TestTask",
        task_description="Task created by Python",
        task_command="main.bat",
        task_arguments="",
        start_time="14:30",
        repeat_interval="PT1H",
        # Example usage (continued)
        user_name=os.getenv("USERNAME"),  # Optional: Replace with actual username if needed
        password=os.getenv("PASSWORD")  # Optional: Replace with actual password if needed
    )

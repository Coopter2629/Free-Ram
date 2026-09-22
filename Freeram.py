import subprocess
import time

# Set how many windows you want to open
num_windows = 10

for i in range(num_windows):
    # '/c' tells cmd to execute a command (or nothing) and immediately exit
    subprocess.Popen(["start", "cmd", "/c"], shell=True)
    
    # Remove this sleep line entirely if you want maximum instant speed
    time.sleep(0.01)

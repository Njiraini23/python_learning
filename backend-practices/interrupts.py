import sys
import signal

# Initialize variables to hold statistics
total_file_size = 0
status_code_count = {}

# Define a function to print statistics
def print_statistics():
    print("Total file size:", total_file_size)
    for status_code in sorted(status_code_count.keys()):
        print(f"{status_code}: {status_code_count[status_code]}")

# Handle keyboard interruption (CTRL + C)
def signal_handler(sig, frame):
    print("\nKeyboardInterrupt detected. Printing statistics:")
    print_statistics()
    sys.exit(0)

# Attach the signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    line_counter = 0
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()
        
        if len(parts) >= 10 and parts[8].isdigit():
            ip, date, request, status_code, file_size = parts[0], parts[3][1:], parts[5], int(parts[8]), int(parts[9])
            if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                total_file_size += file_size
                if status_code in status_code_count:
                    status_code_count[status_code] += 1
                else:
                    status_code_count[status_code] = 1
                
                line_counter += 1
                
                if line_counter % 10 == 0:
                    print_statistics()
        else:
            continue

except KeyboardInterrupt:
    print("\nKeyboardInterrupt detected. Printing statistics:")
    print_statistics()


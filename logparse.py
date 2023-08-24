from collections import defaultdict

def print_statistics(stats):
    total_size = sum(stats['file_size'])
    print(f"Total file size: {total_size}")
    
    for status_code in sorted(stats['status_codes']):
        count = stats['status_codes'][status_code]
        print(f"{status_code}: {count}")

def process_line(line, stats):
    parts = line.split()
    
    if len(parts) != 10:
        return
    
    ip, _, _, _, _, _, request, status_code, file_size, _ = parts
    
    if not status_code.isdigit():
        return
    
    status_code = int(status_code)
    file_size = int(file_size)
    
    stats['file_size'].append(file_size)
    stats['status_codes'][status_code] += 1
    stats['line_count'] += 1
    
    if stats['line_count'] % 10 == 0:
        print_statistics(stats)

def main():
    stats = {'file_size': [], 'status_codes': defaultdict(int), 'line_count': 0}
    
    try:
        while True:
            line = input()
            process_line(line, stats)
    except KeyboardInterrupt:
        pass
    
    print_statistics(stats)

if __name__ == "__main__":
    main()


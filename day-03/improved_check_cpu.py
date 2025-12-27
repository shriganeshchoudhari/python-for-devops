import psutil

def get_cpu_threshold():
    """Prompt user for CPU threshold and validate input."""
    while True:
        try:
            threshold = int(input("Enter the CPU Threshold: "))
            return threshold
        except ValueError:
            print("Invalid input – please enter a numeric value.")

def check_cpu(threshold):
    """Check current CPU usage against the threshold."""
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        print("Current CPU %:", cpu_usage)
        if cpu_usage > threshold:
            print("CPU Alert Email sent...")  # placeholder for email logic
        else:
            print("CPU in Safe state...")
    except Exception as e:
        print(f"Unexpected error while checking CPU: {e}")

def main():
    threshold = get_cpu_threshold()
    check_cpu(threshold)

if __name__ == "__main__":
    main()

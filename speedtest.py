import csv
import subprocess
import time

# Set the number of seconds between each speedtest
interval = 20 # 10 minutes

# Set the number of tests to run
num_tests = 5 # 1 hour

# Open a CSV file for writing
with open('speedtest_results.csv', mode='w') as csv_file:
    fieldnames = ['Timestamp', 'Ping (ms)', 'Download (Mbps)', 'Upload (Mbps)']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    # Perform the tests
    for i in range(num_tests):
        # Get the current time
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

        # Run the speedtest command
        result = subprocess.run(['speedtest-cli', '--simple'], capture_output=True, text=True)

        # Parse the output
        lines = result.stdout.split('\n')
        ping = lines[0].split(' ')[1]
        download = lines[1].split(' ')[1]
        upload = lines[2].split(' ')[1]

        # Write the results to the CSV file
        writer.writerow({'Timestamp': timestamp,
                         'Ping (ms)': ping,
                         'Download (Mbps)': download,
                         'Upload (Mbps)': upload})

        # Wait for the specified interval before running the next test
        time.sleep(interval)
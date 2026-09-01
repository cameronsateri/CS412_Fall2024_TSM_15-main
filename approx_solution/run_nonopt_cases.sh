#!/bin/bash

# Make sure the Python script is executable
chmod +x cs412_tsp_approx.py

# Define the directory containing the test case files
test_case_dir="test_cases"  # Change this to your actual directory path

# Define test case files
# test_cases=("test_case_1.txt" "test_case_2.txt" "test_case_3.txt" "test_case_4.txt" \
# "test_case_5.txt" "test_case_6.txt" "test_case_7.txt")
test_cases=("test_case_8.txt" "test_case_9.txt")

# Run each test case
for test in "${test_cases[@]}"
do
    test_file="$test_case_dir/$test"  # Full path to the test case file

    if [[ -f "$test_file" ]]; then  # Check if the file exists
        echo "Running $test..."
        
        # Record start time in nanoseconds
        start_time=$(date +%s%N)
        
        # Run the Python script
        python3 cs412_tsp_approx.py < "$test_file"
        
        # Record end time in nanoseconds
        end_time=$(date +%s%N)
        
        # Calculate runtime in milliseconds
        runtime=$(( (end_time - start_time) / 1000000 ))
        
        echo "Time taken for $test: $runtime milliseconds"
        echo "-------------------------------"
    else
        echo "Test file $test_file not found! Skipping..."
        echo "-------------------------------"
    fi
done

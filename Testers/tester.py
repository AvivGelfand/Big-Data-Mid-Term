import subprocess

def test_count_top_diff_freq_words():
    # Path to the script to test
    script_path = 'count_top_diff_freq_words.py'
    # Input files and the number of top differences to find
    input_files = ['sample1.txt', 'sample2.txt']
    k = 3
    
    # Execute the script with subprocess
    result = subprocess.run(['python3', script_path] + input_files + [str(k)], capture_output=True, text=True)
    
    # Expected output (modify this based on your manual calculations)
    expected_output = """
bla: 0.3333333333333333
aviv: 0.3333333333333333
lorem: 0.16666666666666666
"""
    # Clean up the actual output for comparison
    actual_output = result.stdout.strip()
    
    # Compare the actual output to the expected output
    if actual_output == expected_output.strip():
        print("Test Passed!")
    else:
        print("Test Failed!")
        print("Expected output:")
        print(expected_output)
        print("Actual output:")
        print(actual_output)

# Run the test
test_count_top_diff_freq_words()

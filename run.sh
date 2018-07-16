#!/bin/bash

# Run the code on the sample data
python3 ./src/pharmacy_counting.py ./input/itcont.txt ./output/top_cost_drug.txt

# Test if the returned output is matches the sample output.
python3 ./src/compare_files.py ./output/sample_output.txt ./output/top_cost_drug.txt
# python3 ./src/pharmacy_counting.py ./input/de_cc_data.txt ./output/top_cost_drug.txt
# python3 ./src/pharmacy_counting.py ./insight_testsuite/tests/test_1/input/itcont.txt ./insight_testsuite/tests/test_1/output/top_cost_drug.txt
# python3 ./src/pharmacy_counting.py ./insight_testsuite/tests/larger_data/input/itcont.txt ./insight_testsuite/tests/larger_data/output/top_cost_drug.txt

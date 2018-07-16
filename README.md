# Scripts for Insight Data Engineering coding challenge
This GitHub repository contains my solution to the [coding challenge](https://github.com/InsightDataScience/pharmacy_counting) for the Fellows Program organized by [Insight Data Science](https://www.insightdatascience.com/).

Given a comma separated input file with 5 columns, e.g.,

```
id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
1000000001,Smith,James,AMBIEN,100
1000000002,Garcia,Maria,AMBIEN,200
1000000003,Johnson,James,CHLORPROMAZINE,1000
1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
1000000005,Smith,David,BENZTROPINE MESYLATE,1500
```
the script generates a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which is listed in descending order based on the total drug cost and if there is a tie, drug name. For example, the output will be the following for the above file.
```
drug_name,num_prescriber,total_cost
CHLORPROMAZINE,2,3000
BENZTROPINE MESYLATE,1,1500
AMBIEN,2,300
```
## Summary
The `pharmacy_counting.py` script reads the input file line by line and creates two dictionaries `drug_cost` (i.e, `{drug_name:total_cost, }`) to keep track of drug costs and `doctor_names` (i.e., `{drug_name:unique_doctor_names}`) to keep track of unique doctor names for each drug. Consequently, the dictionary `drug_cost` is sorted by the value (and key if there is a tie) and written in the desired comma separated output format. This script also performs a basic data cleaning such as getting rid of commas inside quotations. This ensures each row has 5 columns when split on commas.

## Instructions
To execute the script move to the main directory of the project and run the following in the terminal:

```
python ./src/pharmacy_counting.py ./input/itcont.txt ./output/top_cost_drug.txt
```

Last two arguments should be input and output files, respectively.

Alternatively, you can execute `./run.sh` script to run the codes for a sample file and perform a unit test.

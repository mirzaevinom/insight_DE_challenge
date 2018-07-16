"""
Given a comma separated input file with 5 columns, e.g.,

```
id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
1000000001,Smith,James,AMBIEN,100
1000000002,Garcia,Maria,AMBIEN,200
1000000003,Johnson,James,CHLORPROMAZINE,1000
1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
1000000005,Smith,David,BENZTROPINE MESYLATE,1500
```
the script generates a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which is listed in descending order based on the total drug cost and if there is a tie, drug name. E.g.,
```
drug_name,num_prescriber,total_cost
CHLORPROMAZINE,2,3000
BENZTROPINE MESYLATE,1,1500
AMBIEN,2,300
```

"""

import sys

input_fname, output_fname = sys.argv[1:]

# Keeps track of total cost for each drug
drug_cost = dict()

# Keeps track of unique doctor names for each drug
doc_names = dict(set())

# Track number of lines read
n_lines = 0
print('\nProcessing the input file:', input_fname, '\n')
with open(input_fname, 'rb') as inp_f:

    prescription = inp_f.readline()
    prescription = inp_f.readline()

    while len(prescription) > 0:
        # Decode to string for easier manipulation
        prescription = prescription.decode('utf8')
        n_lines += 1

        # Print progress every million lines
        if n_lines % 10**6 == 0:
            print('Number of lines processed:', n_lines//10**6, 'million')

        # Strip commas inside quoted text
        if prescription.find('"') >= 0:

            start = prescription.find('"')
            # Strip all commas inside all the quotations
            while start >= 0:
                end = prescription[start+1:].find('"')
                if end >= 0:
                    end = end+start+1
                prescription = prescription[:start]+prescription[start:end+1].replace(',', '')+prescription[end+1:]
                start = prescription[end+1:].find('"')

        prescription = prescription.split(',')

        # Make sure that each row has 5 columns
        if len(prescription) != 5:
            print('\033[91mFAIL\033[0m: A row must have 5 columns but found this row')
            print(','.join(prescription))
            sys.exit(0)
            
        # Doctor name
        doctor = ' '.join(prescription[1:3])

        # Try accesing the key, if not create that key
        try:
            doc_names[prescription[3]].add(doctor)
            drug_cost[prescription[3]] += float(prescription[-1])
        except KeyError:
            doc_names[prescription[3]] = {doctor}
            drug_cost[prescription[3]] = float(prescription[-1])

        prescription = inp_f.readline()

print('Total number of lines processed:',  "{:,}".format(n_lines))

# Write the output file
with open(output_fname, 'wb') as out_f:
    # Write header of the file
    out_f.write(b'drug_name,num_prescriber,total_cost\n')

    # Sort the keys by the values of drug_cost and if there is a tie, drug name.
    for drug, value in sorted(drug_cost.items(), key=lambda x: (x[1], x[0]), reverse=True):
        # Write to the output file in descending order
        next_line = ','.join([drug, str(len(doc_names[drug])), str(round(drug_cost[drug], 2))])
        next_line += '\n'
        out_f.write(bytes(next_line, 'utf8'))


# Open and print top 10 lines of the output file
print('\nTop 5 lines of the output file\n')
with open(output_fname, 'rb') as out_f:

    a_line = out_f.readline()
    n_lines = 0
    while len(a_line) > 0 and n_lines < 6:
        n_lines += 1
        print(a_line)
        a_line = out_f.readline()

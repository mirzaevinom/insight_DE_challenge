import sys

input_fname, output_fname = sys.argv[1:]

# Keeps record of total cost for each drug
drug_cost = dict()

# Keeps record of unique doctor names for each drug
doc_names = dict(set())

n_lines = 0

with open(input_fname, 'rb') as inp_f:

        prescription = inp_f.readline()
        prescription = inp_f.readline()

        while len(prescription)>0:
            n_lines +=1
            if n_lines%10**6==0:
                print(n_lines)

            prescription = prescription.split(b',' )
            doctor = b' '.join( prescription[1:3] )

            try:
                doc_names[ prescription[3] ].add(doctor)
                drug_cost[ prescription[3] ] += float(prescription[-1])
            except KeyError:
                doc_names[ prescription[3] ] = {doctor}
                drug_cost[ prescription[3] ] = float(prescription[-1])

            prescription = inp_f.readline()

# Write the output file
with open(output_fname, 'wb') as out_f:
    # Write header of the file
    out_f.write(b'drug_name,num_prescriber,total_cost\n')

    # Sort the keys by the values of drug_cost first
    for drug in sorted(drug_cost, key=drug_cost.get, reverse=True):

        # Write to the output file in descending order
        next_line = b','.join( [drug, bytes( str(len(doc_names[drug])) , 'utf8' ),
                                bytes( str( int(drug_cost[drug])) , 'utf8' ) ] )
        next_line +=b'\n'
        out_f.write(next_line)


# Open and print top 10 lines of the output file

print('\nTop 5 lines of the output file\n')
with open(output_fname, 'rb') as out_f:

    a_line = out_f.readline()
    n_lines = 0
    while len(a_line)>0 and n_lines<6:
        n_lines +=1
        print(a_line)
        a_line = out_f.readline()

import sys

input_fname, output_fname = sys.argv[1:]

drug_cost = dict()
doc_names = dict(list())

with open(input_fname, 'rb') as inp_f:

        prescription = inp_f.readline()
        prescription = inp_f.readline()
        # print(dir(prescription))
        while len(prescription)>0:
            print(prescription)
            prescription = prescription.split(b',' )
            doctor = b' '.join( prescription[1:3] )

            if prescription[3] in drug_cost.keys():
                if doctor not in doc_names[ prescription[3] ]:
                    doc_names[ prescription[3] ].append(doctor)

                drug_cost[ prescription[3] ] += int(prescription[-1])
            else:
                doc_names[ prescription[3] ] = [doctor]
                drug_cost[ prescription[3] ] = int(prescription[-1])

            prescription = inp_f.readline()

with open(output_fname, 'wb') as out_f:
    out_f.write(b'drug_name,num_prescriber,total_cost\n')

    for drug in sorted(drug_cost, key=drug_cost.get, reverse=True):
        next_line = b','.join( [drug, bytes( str(len(doc_names[drug])) , 'utf8' ),
                                bytes( str(drug_cost[drug]) , 'utf8' ) ] )
        next_line +=b'\n'
        out_f.write(next_line)
#
# with open('../output/top_cost_drug.txt', 'rb') as out_f:
#
#     a_line = out_f.readline()
#
#     while len(a_line)>0:
#         print(a_line)
#         a_line = out_f.readline()

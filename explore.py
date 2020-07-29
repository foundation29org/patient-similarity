from patient_similarity.__main__ import compare_side_by_side

print(compare_side_by_side([['HP:0000365', '0000005']], [['HP:0000006']], 'data/hp.obo', 'data/phenotype_annotation.tab'))
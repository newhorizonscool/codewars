def DNA_strand(dna):
    dna_compl = ''
    for i in range(len(dna)):
        if dna[i] == 'A':
            dna_compl = dna_compl + 'T'
        if dna[i] == 'T':
            dna_compl = dna_compl + 'A'
        if dna[i] == 'C':
            dna_compl = dna_compl + 'G'
        if dna[i] == 'G':
            dna_compl = dna_compl +  'C'
        print(type(dna_compl))
    return dna_compl
    
print(DNA_strand("GTAT"))

def to_rna(dna_strand):
    for c in dna_strand:
        if c not in set('CGTA'):
            raise Exception("Invalid input, please input valid DNA strand.")
    dna_strand = dna_strand.replace('G', '1')
    dna_strand = dna_strand.replace('C', 'G')
    dna_strand = dna_strand.replace('A', 'U')
    dna_strand = dna_strand.replace('T', 'A')
    dna_strand = dna_strand.replace('1', 'C')
    return dna_strand

## RENAME this file YourLastName_OOP_FinalProject_2023.py

##Assignment: Add to the constructor and methods of a parent class and child classes
##            which inherit the base class properties. NOTE: You are not allowed
##            to import any specialized libraries for this project (e.g., no Biopython)
##            The idea is for you to write these methods from scratch.

## Begin with the parent Seq class and the child DNA class we created in lecture below.
## 

import re
import doctest

### Seq Class
#
#  Constructor:
#  (1) Use the string functions upper and strip to clean up self.sequence.
#  (2) Add a variable self.kmers to the constructor and make it equal to an empty list.

#  Methods:
#  (1) Add a method called make_kmers that makes overlapping kmers of a given length from self.sequence
#      appends these to self.kmers. Default kmer parameter=3.
#  (2) Add a method called fasta that returns a fasta formatted string like this:
#      >species gene
#      AGATTGATAGATAGATAT

class Seq:

    def __init__(self,sequence,gene,species):
        """
        >>> s = Seq("atgCta", "geneX", "E.coli")
        >>> s.sequence
        'ATGCTA'
        >>> s.kmers
        []
        """
        self.sequence=sequence
        self.gene=gene
        self.species=species
        self.sequence=sequence.strip().upper()
        self.kmers=[]
        
    def make_kmers(self, k=3):
        """
        >>> s = Seq("ATGCTA", "geneX", "E.coli")
        >>> s.make_kmers(3)
        ['ATG', 'TGC', 'GCT', 'CTA']
        """
        for i in range(len(self.sequence) - k + 1):
            kmer = self.sequence[i:i+k]
            self.kmers.append(kmer)
        return self.kmers

    def __str__(self):
        return self.sequence

    def print_record(self):
        print(self.species + " " + self.gene + ": " + self.sequence)


    def fasta(self):
        """
        >>> s = Seq("ATGC", "geneX", "E.coli")
        >>> s.fasta()
        '>E.coli geneX\\nATGC'
        """
        return ">" + self.species + " " + self.gene + "\n" + self.sequence


### DNA Class: INHERITS Seq class
#   
#  Constructor:
#  Use re.sub to change any non nucleotide characters in self.sequence into an 'N'.
#      re.sub('[^ATGCU]','N',sequence) will change any character that is not a
#      capital A, T, G, C or U into an N. (Seq already uppercases and strips.)

#  Methods:
#  (1) Add a method called print_info that is like print_record, but adds geneid and an
#      empty space to the beginning of the string.
#  (2) Add a method called reverse_complement that returns the reverse complement of
#      self.sequence
#  (3) Add a method called six_frames that returns all 6 frames of self.sequence
#      This include the 3 forward frames, and the 3 reverse complement frames

class DNA(Seq):

    def __init__(self,sequence,gene,species,geneid,**kwargs):
        """
        >>> d = DNA("ATGXTC", "geneY", "E.coli", "E23")
        >>> d.sequence
        'ATGNTC'
        """
        super().__init__(sequence,gene,species)
        self.geneid=geneid
        self.sequence=re.sub('[^ATGC]','N', self.sequence)
 
    def analysis(self):
        """
        >>> d = DNA("GCGC", "geneY", "E.coli", "E23")
        >>> d.analysis()
        4
        """
        
        gc=len(re.findall('G',self.sequence)) + len(re.findall('C',self.sequence))
        return gc

    def print_info(self):
        print(' ' + self.geneid + ' ' + self.species + self.gene + ': ' + self.sequence)

    def reverse_complement(self):
        """
        >>> d = DNA("ATGC", "geneY", "E.coli", "E23")
        >>> d.reverse_complement()
        'GCAT'
        """
        complements = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
        result = ''.join([complements.get(base, 'N') for base in reversed(self.sequence)])
        return result   

    def six_frames(self):
        """
        >>> d = DNA("ATGCGA", "geneY", "E.coli", "E23")
        >>> len(d.six_frames())
        6
        """
        forward_frames = [self.sequence[i:] for i in range(3)]
        rev_comp_seq = self.reverse_complement()
        reverse_frames = [rev_comp_seq[i:] for i in range(3)]
        return forward_frames + reverse_frames


### RNA Class:  INHERITS DNA class
#  
#  Construtor:
#  Use the super() function (see DNA Class example).
#  (1) Automatically change all Ts to Us in self.sequence. 
#  (2) Add self.codons equals to an empty list

#  Methods:
#  (1) Add make_codons which breaks the self.sequence into 3 letter codons
#      and appends these codons to self.codons unless they are less than 3 letters long.
#  (2) Add translate which uses the Global Variable standard_code below to
#      translate the codons in self.codons and returns a protein sequence.

standard_code = {
     "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S",
     "UCC": "S", "UCA": "S", "UCG": "S", "UAU": "Y", "UAC": "Y",
     "UAA": "*", "UAG": "*", "UGA": "*", "UGU": "C", "UGC": "C",
     "UGG": "W", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
     "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAU": "H",
     "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R",
     "CGA": "R", "CGG": "R", "AUU": "I", "AUC": "I", "AUA": "I",
     "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
     "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S",
     "AGC": "S", "AGA": "R", "AGG": "R", "GUU": "V", "GUC": "V",
     "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A",
     "GCG": "A", "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
     "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

class RNA(DNA):
    def __init__(self, sequence, gene, species, geneid, **kwargs):
        super().__init__(sequence, gene, species, geneid, **kwargs)
        Seq.__init__(self, sequence, gene, species)
        self.geneid = geneid
        self.sequence = self.sequence.replace('T', 'U')
        self.sequence = re.sub('[^AUGC]', 'N', self.sequence)
        self.codons = []
        
    def make_codons(self):
        """
        >>> r = RNA("AUGGCUAA", "geneZ", "E.coli", "E40")
        >>> r.make_codons()
        >>> r.codons
        ['AUG', 'GCU']
        """
        for i in range(0, len(self.sequence) - 2, 3):
            codon = self.sequence[i:i + 3]
            if len(codon) == 3:
                self.codons.append(codon)
                
    def translate(self):
        """
        >>> r = RNA("AUGGCUUAA", "geneZ", "E.coli", "E40")
        >>> r.make_codons()
        >>> r.translate()
        'MA'
        """
        protein = ''
        for codon in self.codons:
            if 'N' in codon:
                protein += 'X'
            elif codon in standard_code:
                amino_acid = standard_code[codon]
                if amino_acid == '*':
                    break
                protein += amino_acid
            else:
                protein += 'X'
        return protein

### Protein Class: INHERITS Seq class
#
#  Construtor:
#  Use the super() function (see DNA Class example).
#  Use re.sub to change any non LETTER characters in self.sequence into an 'X'.

#  Methods:
#  The next 2 methods use a kyte_doolittle and the aa_mol_weights dictionaries.
#  (2) Add total_hydro, which return the sum of the total hydrophobicity of a self.sequence
#  (3) Add mol_weight, which returns the total molecular weight of the protein
#      sequence assigned to the protein object.


kyte_doolittle={'A':1.8,'C':2.5,'D':-3.5,'E':-3.5,'F':2.8,'G':-0.4,'H':-3.2,'I':4.5,'K':-3.9,'L':3.8,
                'M':1.9,'N':-3.5,'P':-1.6,'Q':-3.5,'R':-4.5,'S':-0.8,'T':-0.7,'V':4.2,'W':-0.9,'X':0,'Y':-1.3}

aa_mol_weights={'A':89.09,'C':121.15,'D':133.1,'E':147.13,'F':165.19,
                'G':75.07,'H':155.16,'I':131.17,'K':146.19,'L':131.17,
                'M':149.21,'N':132.12,'P':115.13,'Q':146.15,'R':174.2,
                'S':105.09,'T':119.12,'V':117.15,'W':204.23,'X':0,'Y':181.19}

    
class Protein(Seq):
    def __init__(self, sequence, gene, species, geneid):
        """
       >>> p = Protein("ACD!#", "geneF", "E.coli", "E50")
       >>> p.sequence
       'ACDXX'
        """
        super().__init__(sequence, gene, species)
        self.geneid = geneid
        self.sequence = re.sub(r'[^a-zA-Z]', 'X', self.sequence)
        
    def total_hydro(self):
        """
        >>> p = Protein("ACD", "geneF", "E.coli", "E50")
        >>> round(p.total_hydro(), 1)
        0.8
        """
        hydro_score = 0
        for amino_acid in self.sequence:
            hydro_score += kyte_doolittle[amino_acid]
        return hydro_score
    
    def mol_weight(self):
        """
        >>> p = Protein("ACD", "geneF", "E.coli", "E50")
        >>> round(p.mol_weight(), 2)
        343.34
        """
        total_weight = 0
        for amino_acid in self.sequence:
            if amino_acid in aa_mol_weights:
                total_weight += aa_mol_weights[amino_acid]
        return total_weight

if __name__ == "__main__":
    doctest.testmod(verbose=True)




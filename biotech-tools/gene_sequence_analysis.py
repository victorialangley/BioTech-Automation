"""
gene_sequence_analysis.py
Author: Victoria Langley
Description: This script performs basic analysis on DNA gene sequences.
"""

class GeneSequenceAnalyzer:
    def __init__(self, sequence):
        self.sequence = sequence

    def calculate_gc_content(self):
        gc_count = self.sequence.count('G') + self.sequence.count('C')
        total_count = len(self.sequence)
        gc_content = (gc_count / total_count) * 100
        return gc_content

    def find_codons(self):
        codons = [self.sequence[i:i+3] for i in range(0, len(self.sequence), 3)]
        return codons

if __name__ == "__main__":
    dna_sequence = "ATGTCGTACGTAGCTAGCAGCTAGCTAGCAGCTGACTAGCATGC"
    analyzer = GeneSequenceAnalyzer(dna_sequence)

    gc_content = analyzer.calculate_gc_content()
    print(f"GC Content: {gc_content:.2f}%")

    codons = analyzer.find_codons()
    print("Codons:")
    for index, codon in enumerate(codons, start=1):
        print(f"{index}: {codon}")

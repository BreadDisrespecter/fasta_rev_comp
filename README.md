# fasta_rev_comp
A simple tool that takes fasta files and can produce reverse and complementary strands.
Can be executed like so to create a new fasta file: 

```
fasta_rev_comp.py example.fasta --revcomp > output.fasta
```

Where example.fasta is a downloaded .fasta file.
Requires both scripts (fasta_rev_comp.py and iupac.py) to function.
iupac.py is there to define the corresponding nucleotides, including unknown bases or gaps (eg R,Y,S,K).

--revcomp produces the reverse and complementary strand
--reverse reverses the sequence
--complement produces the complementary sequence without reversing it

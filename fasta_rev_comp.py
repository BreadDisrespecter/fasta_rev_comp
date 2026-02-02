#!/usr/bin/env python3

# Reverse, complement, or reverse-complement FASTA sequences.

import sys
import argparse
from iupac import complement_base

def parse_fasta(handle):
  # Generator yielding (header, sequence) tuples from a FASTA file
  header = None
  seq_chunks = []
  
  for line in handle:
    line = line.rstrip()
    if not line:
      continue
  
    if line.startswith(">"):
      if header is not None:
        yield header, "".join(seq_chunks)
      header = line
      seq_chunks = []
    else:
      seq_chunks.append(line)
    
  if header is not None:
    yield header, "".join(seq_chunks)
      
def transform_sequence(seq: str, reverse=False, complement=False, rna=False) -> str:
  seq = seq.upper()
  if complement:
    seq = "".join(complement_base(b, rna = rna) for b in seq)
  if reverse:
    seq = seq[::-1]
  if rna:
    seq = seq.replace("T","U")
  return seq
    
def main():
  parser = argparse.ArgumentParser(description="Reverse, complement, reverse-complement, or generate RNA transcript from FASTA sequences")
  parser.add_argument("fasta", help="Input FASTA file ('-' for stdin)")
  parser.add_argument("--reverse", action="store_true", help="Reverse sequence")
  parser.add_argument("--complement", action="store_true", help="Complement sequence")
  parser.add_argument("--revcomp", action="store_true", help="Reverse-complement")
  parser.add_argument("--rna", action="store_true", help="Reverse-complement and output as RNA (A <-> U)")

  args = parser.parse_args()

# If --rna is specified, automatically do revcomp:
  if args.rna:
      do_reverse = True
      do_complement = True
  elif args.revcomp:
      do_reverse = True
      do_complement = True
  else:
      do_reverse = args.reverse
      do_complement = args.complement

  if not (do_reverse or do_complement or do_rna):
      parser.error("Must specify --reverse, --complement, --rna, or --revcomp")

    # Open input
  if args.fasta == "-":
      handle = sys.stdin
  else:
      handle = open(args.fasta, encoding="utf-8")

  try:
      for header, seq in parse_fasta(handle):
          new_seq = transform_sequence(
              seq,
              reverse=do_reverse,
              complement=do_complement,
              rna=args.rna,
          )
          print(header)
          for i in range(0, len(new_seq), 60):
              print(new_seq[i:i+60])
  finally:
      if handle is not sys.stdin:
          handle.close()
      
if __name__ == "__main__":
  main()

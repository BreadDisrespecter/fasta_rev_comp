# Complementary nucleotides including ambiguous bases under IUPAC:
DNA_Complement = {
  "A":"T", "T":"A", "C":"G", "G":"C", "R":"Y", # A or G -> T or C
  "Y":"R", # C or T -> G or A
  "S":"S", # G or C
  "W":"W", # A or T
  "K":"M", # G or T -> C or A
  "M":"K", # A or C -> T or A
  "B":"V", # C or G or T -> G or C or A
  "D":"H", # A or G or T -> T or C or A
  "H":"D", # T or C or A -> A or G or T
  "V":"B", # A or C or G -> C or G or T
  "N":"N", # Unknown base
  "-":"-", # Gap
  ".":".", # Gap
  }
  
  # RNA Complement
RNA_Complement = {
    ** DNA_Complement, "A":"U", "U":"A", "T":"A", # Adjust for DNA input
    }
    
def complement_base(base:str, rna:bool = False) -> str:# Returns complements of nucleotides
      base = base.upper()
      table = RNA_Complement if rna else DNA_Complement
      return table.get(base, base)
    

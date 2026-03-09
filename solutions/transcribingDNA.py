def transcribe(dna):
    rna = dna.replace("T", "U")
    return rna

if __name__ == "__main__":
    with open ("files/rosalind_rna.txt", "r") as f:
        dna = f.read()
        rna = transcribe(dna)
        print(rna)
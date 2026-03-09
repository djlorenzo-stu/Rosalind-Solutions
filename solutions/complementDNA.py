def complement(data):
    complement = {"A": "T", "C": "G", "G": "C", "T": "A"}
    result = ""
    for base in data:
        result += complement[base]
    return result

if __name__ == "__main__":
    with open ("files/rosalind_revc.txt", "r") as f:
        data = f.read().strip()
        result = complement(data)
        reversed_dna = result[::-1]
        print(reversed_dna)
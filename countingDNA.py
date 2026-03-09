def countingDNA(data):
        countA = data.count("A")
        countC = data.count("C")
        countG = data.count("G")
        countT = data.count("T")
        print(countA, countC, countG, countT)
        
if __name__ == "__main__":
    with open ("files/file.txt", "r") as f:
        data = f.read()
        countingDNA(data)
    
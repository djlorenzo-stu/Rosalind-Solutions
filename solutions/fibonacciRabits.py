def fiboRab(n,k):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fiboRab(n-1,k) + k * fiboRab(n-2,k)
    
if __name__ == "__main__":
    with open ("files/rosalind_fib.txt", "r") as f:
        data = f.read().strip().split()
        n = int(data[0])
        k = int(data[1])
        result = fiboRab(n,k)
        print(result)

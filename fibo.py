

def recursive_nth_fibo(n):
    if n == 0:
        return n
    if n == 1:
        return n
    else:
        return recursive_nth_fibo(n-1) + recursive_nth_fibo(n-2)

    # sequence = [0,1]
    # while n > 1:
    #     sequence.append(recursive_nth_fibo(n)[n - 1] + recursive_nth_fibo(n)[n - 2])

def main():
    number = int(input("Zadej cislo: "))
    print(recursive_nth_fibo(number))

if __name__ == "__main__":
    main()

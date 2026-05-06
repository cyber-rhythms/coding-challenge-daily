if __name__ == "__main__":
    M, N = map(int, input().split())
    num_top_lines = int((N - 1) / 2)

    for i in range(num_top_lines):
        print(((".|." * i) + ".|." + (".|." * i)).center(M, "-"))

    print("WELCOME".center(M, "-"))

    for i in range(num_top_lines -1, -1, -1):
        print(((".|." * i) + ".|." + (".|." * i)).center(M, "-"))
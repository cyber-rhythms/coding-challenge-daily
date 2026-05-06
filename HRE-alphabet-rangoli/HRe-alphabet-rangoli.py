letters = "abcdefghijklmnopqrstuvwxyz"

def print_rangoli(n):

    num_lines_top = n - 1
    centre_line = "-".join(letters[n-1:0:-1] + letters[0] + letters[1:n])
    line_size = len(centre_line)

    # Construct the top (n - 1) lines.
    for i in range(num_lines_top, 0, -1):
        print("-".join(letters[n-1:i:-1] + letters[i] + letters[1+i:n]).center(line_size, "-"))

    # Construct the centre line and the bottom (n-1) lines.
    for i in range(num_lines_top + 1):
        print("-".join(letters[n-1:i:-1] + letters[i] + letters[1+i:n]).center(line_size, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
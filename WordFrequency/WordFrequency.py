def print_wds(data):
    for x in sorted(data.keys()):
        print(x, "::", data[x])


def word_freq(fptr):
    freq = {}
    line = fptr.readline()
    punct_chars = (",", ".", ":", ";", "(", ")", "{", "}", "[", "]", "'", '"', "!", "-", "?")
    while line:
        for c in punct_chars:
            line = line.replace(c, "")
        words = line.split()

        for word in words:
            tmp = word.lower()
            freq[tmp] = freq.get(tmp, 0) + 1
        line = fptr.readline()
    return freq

def main():
    answer = input("Would you like to enter a text file? Yes or No.")

    while answer.lower() == "yes":
        file_name = input("Please enter your file name.")

        try:
            f = open(file_name, "r")
        except IOError as e:
            file_name = input("The file name is incorrect. Please enter another file name.")
        else:
            frq_wd = word_freq(f)
            print_wds(frq_wd)
            f.close()

        answer = input("Would you like to enter a text file? Yes or No.")

main()



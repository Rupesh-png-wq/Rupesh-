# String Operation Function

def rev_string(s):
    return s[::-1]

def count_vowel(s):
    vowel = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowel:
            count += 1
    return count

def find_max(lst):
    return max(lst)

def sum_list(lst):
    return sum(lst)

def main():
    string = input("Enter a String: ")
    print("Reversed string:", rev_string(string))
    print("Count the number of vowel:", count_vowel(string))

    lst = list(map(int, input("Enter list elements (space-separated): ").split()))
    print("Maximum value of list:", find_max(lst))
    print("Sum of list:", sum_list(lst))

if __name__ == "__main__":
    main()
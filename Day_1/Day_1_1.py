# Written by Stephen Berkner for 
# Advent of Code 2020 Day 1 Part 1

def calculate_product(vals):
    for i in range(0,len(vals)):
        for j in range(0,len(vals)):
            if vals[i] + vals[j] == 2020:
                return (vals[i] * vals[j])

if __name__ == "__main__":
    nums = []

    with open('input.txt') as f:
        for line in f:
            nums.append(int(line))

    print(calculate_product(nums))
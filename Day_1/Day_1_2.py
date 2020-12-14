# Written by Stephen Berkner for 
# Advent of Code 2020 Day 1 Part 2

def calculate_product(vals):
    for i in range(0,len(vals)):
        for j in range(0,len(vals)):
            for k in range(0, len(vals)):
                if vals[i] + vals[j] + vals[k] == 2020:
                    return (vals[i] * vals[j] * vals[k])

if __name__ == "__main__":
    nums = []

    with open('input.txt') as f:
        for line in f:
            nums.append(int(line))

    print(calculate_product(nums))
# Written by Stephen Berkner for 
# Advent of Code 2020 Day 2 Part 2

if __name__ == "__main__":

    num_valid = 0

    with open('Day_2/input.txt') as f:

        for line in f:
            test_data = line.split(":")[0]
            test_range = test_data.split(" ")[0]
            first_pos = int(test_range.split("-")[0])
            second_pos = int(test_range.split("-")[1])
            test_letter = str(test_data.split(" ")[1])
            to_test = str(line.split(":")[1])

            if (to_test[first_pos] == test_letter) ^ (to_test[second_pos] == test_letter):
                num_valid += 1

        print(num_valid)
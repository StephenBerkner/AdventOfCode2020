# Written by Stephen Berkner for 
# Advent of Code 2020 Day 2 Part 1


if __name__ == "__main__":
    num_valid = 0

    with open('input.txt') as f:
        for line in f:
            test_data = line.split(":")[0]
            
            test_range = test_data.split(" ")[0]
            
            min = int(test_range.split("-")[0])
            max = int(test_range.split("-")[1])
            
            test_letter = str(test_data.split(" ")[1])

            to_test = str(line.split(":")[1])

            num_occurences = to_test.count(test_letter)

            if (num_occurences >= min) and (num_occurences <= max):
                num_valid += 1
        
        print(num_valid)
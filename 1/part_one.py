file_name = "input.txt"

with open(file_name) as input_file:
    sum = 0

    for line in input_file:
        first_value = -1
        last_value = -1

        for value in line:
            if (value.isnumeric()):
                if first_value == -1:
                    first_value = int(value)
                    last_value = int(value)
                else:
                    last_value = int(value)

        value_in_line = (int(str(first_value) + str(last_value)))
        sum += value_in_line

    print(sum)


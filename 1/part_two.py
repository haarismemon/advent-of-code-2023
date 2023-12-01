file_name = "input.txt"

def check(digits, word):
    for d in digits:
        if d in word:
            return (True, d)
    
    return (False, '')

with open(file_name) as input_file:
    digits = {'one': '1', 'two' : '2', 'three': '3', 'four': '4', 'five' : '5', 'six' : '6', 'seven': '7', 'eight' : '8', 'nine': '9'}

    sum = 0

    for line in input_file:
        line = line.replace('\n','')
        first_value = 0
        last_value = 0

        replacements_to_do = []

        word = ''
        for c in line:
            if(c.isalpha()):
                word += c

                check_bool, found_word = check(digits.keys(), word)

                if check_bool:
                    replacements_to_do.append(found_word)
                    # print(found_word)
                    word = ''
            elif(c.isnumeric()):
                word = ''

        # print(replacements_to_do)

        for r in replacements_to_do:
            num = digits.get(r)
            if num:
                line = line.replace(r, num)

        for value in line:
            if (value.isnumeric()):
                if first_value == 0:
                    first_value = int(value)
                    last_value = int(value)
                else:
                    last_value = int(value)

        value_in_line = (int(str(first_value) + str(last_value)))

        print(line + ' = ' + str(value_in_line))

        sum += value_in_line

    print(sum)

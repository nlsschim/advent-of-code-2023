print('start')

int_list = ['1','2','3','4','5','6','7','8','9']

string_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

tot_list = int_list + string_list

sum = 0
with open('input.txt','r') as file:
    for line in file:
        line_value = []
        indices = []
        digits = []

        for i, digit in enumerate(tot_list):
            if line.count(digit) == 1:
                digits.append(digit)
                indices.append(line.index(digit))
            elif line.count(digit) > 1:
                digits.append(digit)
                indices.append(line.index(digit))
                digits.append(digit)
                indices.append(line.rindex(digit))
                
                

        min_index = min(indices)
        max_index = max(indices)
        line_value.append(digits[indices.index(min_index)])
        line_value.append(digits[indices.index(max_index)])

        first_digit = line_value[0]
        second_digit = line_value[-1]

        if first_digit in string_list:
            first_digit = str(string_list.index(first_digit) + 1)

        if second_digit in string_list:
            second_digit = str(string_list.index(second_digit) + 1)

        two_digit = first_digit + ''.join(str(second_digit))
        sum += int(two_digit)


        


        print(digits)
        print(indices)
        print(line_value)
        print(two_digit)
        print()
print(sum)
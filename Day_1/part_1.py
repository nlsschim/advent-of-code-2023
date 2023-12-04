print('start')

int_list = ['1','2','3','4','5','6','7','8','9']
sum = 0
with open('input.txt','r') as file:
    for line in file:
        line_value = []
        for i in range(len(line)):
            if line[i] in int_list:
                line_value.append((line[i]))
        first_digit = ''.join(line_value[0])#.join(line_value[-1])
        two_digit_string = first_digit + ''.join(line_value[-1])
        print(two_digit_string)

        print()
        sum += int(two_digit_string)
        #sum += (line_value[0]+line_value[-1])
        #sum += sum(line_value)
print(sum)



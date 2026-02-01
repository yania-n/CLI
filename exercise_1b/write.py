import exercise_1b.add_function as add_function

def write_result(num1, num2, file_name):

    sum_value = add_function.addition(num1, num2)

    with open(file_name, 'a') as f:
            f.write('First number:' + str(num1) + '; Second number:' + str(num2) + '; Sum:' + str(sum_value) + '\n')

if __name__ == "__main__":
      write_result(11,24, 'exercise_1b/test.txt')
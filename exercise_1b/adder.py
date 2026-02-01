import argparse
import exercise_1b.write as write

parser = argparse.ArgumentParser('Adder', description='Simple addition calculator', epilog = 'Enter two numbers (num1), (num2) and get their summed result')
parser.add_argument('num1', type= float , help= 'The first number')
parser.add_argument('num2', type = float, help = 'The second number')
args = parser.parse_args()

num1 = args.num1
num2 = args.num2

write.write_result(num1, num2, 'exercise_1b/result.txt')


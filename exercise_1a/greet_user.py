import argparse
import exercise_1a.greet_function as g
import exercise_1a.write_function as w

parser = argparse.ArgumentParser(description= 'Greet the user')

parser.add_argument('-n', '--name', type=str, default='Yania', help='Enter your name')
parser.add_argument('-a', '--age', type=int, default=30, help='Enter your age')

args = parser.parse_args()


if __name__ == "__main__":
    output = g.greet_fn(args.name,args.age)
    w.write_fn(output, 'exercise_1a/outputs.txt')
    print(output)

# cat filename.txt -> to read the file content in terminal
# cd.. -> to go back one directory in terminal
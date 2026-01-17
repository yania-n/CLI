# User can run either greeting message program or prediction model program
import argparse
import exercise_2a.main as greeting
import exercise_2b.main as predictor

def main():
    parser = argparse.ArgumentParser(description = 'Choose a program to run')
    subparsers = parser.add_subparsers(dest = 'command')
    subparsers.add_parser('greet', parents = [greeting.get_parser()], help = 'Run greeting')
    subparsers.add_parser('predict', parents = [predictor.get_parser()], help = 'Run prediction model')
    args = parser.parse_args()

    if args.command == 'greet':
        greeting.user_greeting(args)
    
    elif args.command == 'predict':
        predictor.predict_price(args)

if __name__ == '__main__':
    main()

'''
Example commands to run the programs:

- For greeting message program -
python3 exercise_3/main greet --name Alice --age 25

- For prediction model program -
python exercise_3/main predict --beds 3 --baths 2 --size 1200 -z 98105
'''
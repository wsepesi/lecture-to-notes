import argparse

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filepath", help="path to the file to be processed")
    args = parser.parse_args()

    if args.filepath:
        print('worked')

if __name__ == '__main__':
    run()
def run():
    import sys
    import argparse

    parser = argparse.ArgumentParser(description='Process the \"Hello World\" message.')
    parser.add_argument('-f', type=str, default="Some file")
    parser.add_argument('--hello_world_message', type=str, default="Hello World...")
    parser.add_argument('--input_data_dir', type=str)
    parser.add_argument('--working_dir', type=str)
    parser.add_argument('--output_data_dir', type=str)
    args = parser.parse_args()

    print(args.hello_world_message)
    print("Argument List:"+str(sys.argv))
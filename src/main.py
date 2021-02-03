from code_usage_tracker.visualisation import DirectoryVisualiser
import argparse


parser = argparse.ArgumentParser("search")
parser.add_argument("directory_path", help="the path to the directory to be searched", type=str)
parser.add_argument("search_expression", help="uses grep to find the `search_expression` in the files", type=str)
args = parser.parse_args()


directory_visualiser = DirectoryVisualiser(directory_path=args.directory_path, include_hidden=False, query=args.search_expression)
directory_visualiser.visualise()



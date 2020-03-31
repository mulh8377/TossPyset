import subprocess

import argparse


def main(project: str, path: str):
	print('hello')

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--project',type=str,required=True)
	parser.add_argument('--path',type=str,required=True)
	args = parser.parse_args()
	
	if args.project and args.path:
		main(args.project, args.path)
		

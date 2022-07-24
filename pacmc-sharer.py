def main():
    from functions import create_script

    import argparse

    parser = argparse.ArgumentParser(
        description="Scans your specified folder for mods downloaded with the PacMC package manager and outputs all valid PacMC mods in the folder.")
    group = parser.add_argument_group()
    
    group.add_argument('archive_path', help='Path to the archive you are pulling mods list from.')
    
    group.add_argument('--file', '-f', action='store', default=[''], nargs=1, metavar=(
        '<file_path>',), help='Path to the output file (if none specified, no file)')
    
    group.add_argument('--copy', '-c', action='store_true',
                       default=False, help='Use this to copy the mod list to the system clipboard.')
    
    group.add_argument('--include-repo', action='store_true',
                       default=False, help='Use this to implement the repo the mod came from into the output.')
    
    py_args = parser.parse_args()
    py_args.file = py_args.file[0]
    create_script(py_args)


if __name__ == '__main__':
    main()

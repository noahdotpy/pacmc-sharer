def main():
    from functions import create_script

    import argparse

    parser = argparse.ArgumentParser(
        description="A Simple Pacmc Archive Sharer.")
    group = parser.add_argument_group()
    group.add_argument(
        'archive_path', help='Path to the archive you want to share.')
    group.add_argument('--file', '-f', action='store', default=['output.sh'], nargs=1, metavar=(
        '<File name>',), help='Where do you want the file to be created?')
    group.add_argument('--game-version', '-gv', action='store', default=[''], nargs=1, metavar=(
        '<Game version>',), help='Which version of minecraft is the archive for?', required=True)
    group.add_argument('--short', '-s', action='store_true', default=False,
                       help='Used to get a short, one-line version of the normal script code.')
    group.add_argument('--no-file', '-nf', action='store_true',
                       default=False, help='Use this to not get a file.')
    group.add_argument('--copy', '-c', action='store_true',
                       default=False, help='Use this copy the final script.')
    args = parser.parse_args()
    create_script(args.archive_path,
                  args.file[0], args.game_version[0], args.short, args.no_file, args.copy)


if __name__ == '__main__':
    main()

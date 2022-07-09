def main():
    from functions import create_script

    import argparse

    parser = argparse.ArgumentParser(
        description="A Simple Pacmc Archive Sharer.")
    group = parser.add_argument_group()
    # group.add_argument('--create-script', '-c', action='store', nargs=3, metavar=('<In-archive path>',
    #                 '<Out-archive name>', '<Out-archive path>'), help='Create a script to share your archive with others.')
    group.add_argument(
        'in_arc_path', help='Path to the archive you want to share.')
    group.add_argument(
        'out_arc_name', help='Name of the archive that will be created on the user\'s machine.')
    group.add_argument(
        'out_arc_path', help='Path to the archive that will be created on the user\'s machine.')
    group.add_argument('--repo', '-r', action='store', default=[''], nargs=1, metavar=(
        '<Repository>',), help='Set the repository that will be used in the script, set to \'\' to make the user decide.')
    group.add_argument('--file', '-f', action='store', default=['output.sh'], nargs=1, metavar=(
        '<File name>',), help='Where do you want the file to be created?')
    group.add_argument('--game-version', '-gv', action='store', default=[''], nargs=1, metavar=(
        '<Game version>',), help='Which version of minecraft is the archive for?', required=True)
    args = parser.parse_args()

    create_script(args.in_arc_path, args.out_arc_name, args.out_arc_path,
                  args.repo[0], args.file[0], args.game_version[0])


if __name__ == '__main__':
    main()

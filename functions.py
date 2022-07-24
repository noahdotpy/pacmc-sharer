from os import listdir
from os.path import isfile, join

import pyperclip

def create_script(py_args):
    mods = []
    files = [f for f in listdir(py_args.archive_path) if isfile(join(py_args.archive_path, f))]
    
    # Checking for valid files and adding them to mods list if True
    for mod_file in files:
        # check if the .jar is a valid pacmc file
        if mod_file.endswith('.pacmc.jar'):
            # modrinth
            if '_mr_' in mod_file:
                splitted = mod_file.split('_mr_')
                mod_repo = "modrinth/"
            # curseforge
            if '_cf_' in mod_file:
                splitted = mod_file.split('_cf_')
                mod_repo = "curseforge/"
            if not py_args.include_repo:
                mod_repo = ""
            mod_slug = splitted[0]
            mods.append(f"{mod_repo}{mod_slug}")

    # Render the output shell script
    mods_list_as_str = " ".join([mod for mod in mods])
    if py_args.file:
        with open(py_args.file, 'w') as out_file:
            print(mods_list_as_str , file=out_file)
            print("INFO: Created file at " + py_args.file)

    if py_args.copy:
        pyperclip.copy(mods_list_as_str )
        print("INFO: Mod list copied to clipboard!")

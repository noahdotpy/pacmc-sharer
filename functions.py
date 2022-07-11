from os import listdir
from os.path import isfile, join

import pyperclip

def render_script(short: bool, game_version: str, valid_files: dict):
    if short:
            return f"""echo -n "Where do you want this new archive? "; read ARC_DIR && echo -n "What do you want your archive to be called? "; read ARC_NAME; echo -n "What repo do you want to use? (modrinth, curseforge, ENTER to choose for each mod) "; read REPO; if [ "$REPO" = "" ]; then echo "Repo: None"; else REPO+="/"; echo "Repo: $REPO"; fi; GAME_VERSION=\'{game_version}\'; pacmc archive create $ARC_NAME $ARC_DIR; pacmc archive version $ARC_NAME --game-version $GAME_VERSION; """r"pacmc install -y -a $ARC_NAME " + ' '.join([valid_files[mod_id]["repo"]+ valid_files[mod_id]["name"] for mod_id in valid_files])
    else:
        return f"""#!/bin/bash      
            
# !! IMPORTANT: YOU NEED TO SET EXECUTABLE PERMS FOR THIS SCRIPT BEFORE RUNNING !!


######## CONFIG ########


# => Archive which the mods will be downloaded to.

# Path to the archive that will be created
echo -n "Where do you want this new archive? "
read ARC_DIR # assign input value into a variable

# Unique name/identifier for the archive that will be created
echo -n "What do you want your archive to be called? "
read ARC_NAME # assign input value into a variable

# => Version of Minecraft (RECOMMENDED NOT TO CHANGE THIS SETTING)
GAME_VERSION=\'{game_version}\'

######## CREATE ARCHIVE AND INSTALL MODS ########

# Creating archive
pacmc archive create $ARC_NAME $ARC_DIR
pacmc archive version $ARC_NAME --game-version $GAME_VERSION

# All the individual install scripts
""" + r"""pacmc install -y -a $ARC_NAME """ + ' '.join([valid_files[mod_id]["repo"] + valid_files[mod_id]["name"] for mod_id in valid_files])

def create_script(archive_path: str, out_file_path: str, game_version: str, short: bool, no_file: bool, copy: bool):
    valid_files = {}
    files = [f for f in listdir(archive_path) if isfile(join(archive_path, f))]
    
    # Checking for valid files and adding them to valid_files if True
    for index, file in enumerate(files):
        if file.endswith('.pacmc.jar'):
            # modrinth
            if '_mr_' in file:
                splitted = file.split('_mr_')
                mod_repo = "modrinth/"
            # curseforge
            if '_cf_' in file:
                splitted = file.split('_cf_')
                mod_repo = "curseforge/"
            mod_name = splitted[0]
            mod_id = splitted[1].split('.pacmc.jar')[0]
            valid_files[mod_id] = {
                'name': mod_name,
                'repo': mod_repo
            }

    # Render the output shell script
    if not no_file:
        with open(out_file_path, 'w') as out_file:
            print(render_script(short, game_version, valid_files), file=out_file)
            print("INFO: Created file at " + out_file_path)

    if copy:
        pyperclip.copy(render_script(short, game_version, valid_files))
        print("INFO: Script copied to clipboard!")

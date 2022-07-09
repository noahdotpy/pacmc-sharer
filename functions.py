import argparse
from os import listdir
from os.path import isfile, join


def create_script(in_dir: str, out_arc_name: str, out_arc_path: str, repo: str, out_file: str, game_version: str):
    # Logic to get the ids and names of mods in the in_dir
    print(in_dir, out_arc_name, out_arc_path, repo, out_file, sep='\n')
    valid_files = {}
    files = [f for f in listdir(in_dir) if isfile(join(in_dir, f))]
    for index, file in enumerate(files):
        splitted = file.split('_mr_')
        mod_name = splitted[0]
        mod_id = splitted[1].split('.pacmc.jar')[0]

        valid_files[mod_id] = {
            'name': mod_name
        }

    # Empty the output file
    with open(out_file, 'w') as file:
        print('', file=file)
        print("Created file at " + out_file)

    # Print output shell script
    if repo:
        repo += '/'
    with open(out_file, 'a') as out_file:
        print(
            f"""#! /bin/bash

######## CONFIG ########

# !! IMPORTANT: YOU MIGHT WANT TO CHANGE THESE VARIABLES !!

# => Location the mods will be downloaded to (default: your mod folder)
# Path to the archive that will be created
ARC_DIR={out_arc_path}
# Unique name/identifier for the archive that will be created
ARC_NAME=\'{out_arc_name}\'

# => Repository to be downloaded from (modrinth, curseforge, etc...)
# ! Set to '' to disable automatic repo choosing
# ! Must have a / at the end ( modrinth/ )
REPO=\'{repo}\'

# => Version of Minecraft that this archive is based on
GAME_VERSION=\'{game_version}\'

######## CREATE ARCHIVE AND INSTALL MODS ########

# Creating archive
pacmc archive create $ARC_NAME $ARC_DIR
pacmc archive version $ARC_NAME --game-version $GAME_VERSION

# All the individual install scripts
"""
            +
            '\n'.join(
                [r'pacmc install ${REPO}' + valid_files[mod_id]["name"] + ' -y -a $ARC_NAME' for mod_id in valid_files]),
            file=out_file
        )

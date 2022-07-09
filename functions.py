from os import listdir
from os.path import isfile, join


def create_script(in_dir: str, out_arc_name: str, out_arc_path: str, repo: str, out_file: str, game_version: str):
    # Logic to get the ids and names of mods in the in_dir
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
            
# !! IMPORTANT: YOU NEED TO SET EXECUTABLE PERMS FOR THIS SCRIPT BEFORE RUNNING !!


######## CONFIG ########


# => Archive which the mods will be downloaded to.

# Path to the archive that will be created
echo -n "Where do you want this new archive? "
read ARC_DIR # assign input value into a variable

# Unique name/identifier for the archive that will be created
echo -n "What do you want your archive to be called? "
read ARC_NAME # assign input value into a variable

# => Repository to be downloaded from (modrinth, curseforge, etc...)
echo -n "What repo do you want to use? (modrinth, curseforge, ENTER to choose for each mod) "
read REPO # assign input value into a variable

if [ "$REPO" = "" ]
then
    echo "Repo: None"
else
    REPO+="/"
    echo "Repo: $REPO"
fi

# => Version of Minecraft (RECOMMENDED NOT TO CHANGE THIS SETTING)
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

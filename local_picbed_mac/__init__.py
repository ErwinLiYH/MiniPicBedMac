import os


# Configurations
TITLE = "MyPicBed"
FILES_DIRECTORY = {
    "default": os.path.expanduser('~/mypicbed/'),
    # "any_other_vault": "path/to/your/vault"
    }
PORT = 20119
COPY_BEVAIOR = "MD"  # "MD", "URL" or "PATH"
import rumps
import os
from AppKit import NSPasteboard, NSPasteboardTypePNG, NSPasteboardTypeTIFF, NSStringPboardType
from PIL import Image
import io
import datetime
from pkg_resources import resource_filename
import pickle
from . import FILES_DIRECTORY
from . import PORT
from . import COPY_BEVAIOR


def read_default_vault():
    with open(resource_filename(__name__, "data/default_vault"), "rb") as f:
        return pickle.load(f)
    
def write_default_vault(vault):
    with open(resource_filename(__name__, "data/default_vault"), "wb") as f:
        pickle.dump(vault, f)

class ClipboardImageSaverApp(rumps.App):
    def __init__(self):
        super(ClipboardImageSaverApp, self).__init__("MyPicbed")
        self.save_folders = FILES_DIRECTORY
        self.save_vault = read_default_vault()
        self.save_folder = self.save_folders[self.save_vault]

        self.vault_selection_menu = rumps.MenuItem(f"Selected Vault: {self.save_vault}")
        for k in self.save_folders.keys():
            self.vault_selection_menu.add(rumps.MenuItem(k, callback=self.change_vault))

        self.menu = ["Save Image From Clipboard", self.vault_selection_menu]

    def change_vault(self, sender):
        self.save_vault = sender.title
        self.save_folder = self.save_folders[self.save_vault]
        self.vault_selection_menu.title = f"Selected Vault: {self.save_vault}"
        write_default_vault(self.save_vault)

    @rumps.clicked("Save Image From Clipboard")
    def save_image(self, _):
        pasteboard = NSPasteboard.generalPasteboard()
        pasteboard_types = pasteboard.types()

        image_data = None
        if NSPasteboardTypePNG in pasteboard_types:
            image_data = pasteboard.dataForType_(NSPasteboardTypePNG)
        elif NSPasteboardTypeTIFF in pasteboard_types:
            image_data = pasteboard.dataForType_(NSPasteboardTypeTIFF)

        if image_data:
            image = Image.open(io.BytesIO(image_data))
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_path = os.path.join(self.save_folder, f"Clipboard_{timestamp}.png")
            image.save(file_path)
            rumps.notification(title="Image Saver", subtitle="Image saved successfully!", message=f"Saved to {file_path}")
            
            # Copy the URL path to the clipboard
            pasteboard.declareTypes_owner_([NSStringPboardType], None)
            if COPY_BEVAIOR == "MD":
                to_copy = f"![](http://127.0.0.1:{PORT}/{self.save_vault}/"+f"Clipboard_{timestamp}.png)"
            elif COPY_BEVAIOR == "URL":
                to_copy = f"http://127.0.0.1:{PORT}/{self.save_vault}/"+f"Clipboard_{timestamp}.png"
            elif COPY_BEVAIOR == "PATH":
                to_copy = file_path
            else:
                to_copy = "COPY_BEVAIOR ERROR"
            pasteboard.setString_forType_(to_copy, NSStringPboardType)
        else:
            rumps.notification(title="Image Saver", subtitle="No image found in clipboard", message="Please copy an image first")

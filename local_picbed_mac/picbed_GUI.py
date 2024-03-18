import rumps
import os
from AppKit import NSPasteboard, NSPasteboardTypePNG, NSPasteboardTypeTIFF, NSStringPboardType
from PIL import Image
import io
import datetime
from . import FILES_DIRECTORY
from . import PORT
from . import COPY_BEVAIOR


class ClipboardImageSaverApp(rumps.App):
    def __init__(self):
        super(ClipboardImageSaverApp, self).__init__("MyPicbed")
        self.menu = ["Save Image From Clipboard"]
        self.save_folder = FILES_DIRECTORY

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
                to_copy = f"![](http://127.0.0.1:{PORT}/files/"+f"Clipboard_{timestamp}.png)"
            elif COPY_BEVAIOR == "URL":
                to_copy = f"http://127.0.0.1:{PORT}/files/"+f"Clipboard_{timestamp}.png"
            elif COPY_BEVAIOR == "PATH":
                to_copy = file_path
            else:
                to_copy = "COPY_BEVAIOR ERROR"
            pasteboard.setString_forType_(to_copy, NSStringPboardType)
        else:
            rumps.notification(title="Image Saver", subtitle="No image found in clipboard", message="Please copy an image first")

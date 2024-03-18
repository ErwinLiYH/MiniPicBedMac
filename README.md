# Local PicBed for MacOS

This project introduces a minimalist local picture hosting solution (PicBed) specifically designed for macOS. It leverages the simplicity and flexibility of [Flask](https://flask.palletsprojects.com) for serving images over the web, and [rumps](https://github.com/jaredks/rumps) for integrating seamlessly with the macOS menu bar.

Features:

- **Clipboard Monitoring**: Automatically saves images copied to the clipboard, streamlining the process of image uploading.

- **URL Copying**: After an image is saved, the URL of the image is immediately copied to the clipboard, making it easy to share or embed the image elsewhere.

This PicBed solution is ideal for users seeking a straightforward and efficient method to manage and share images locally in Markdowns or Obsidian.

## Install

1. Install Python
2. Build a Python environment if you need(optional)
3. Clone the repository
    ```bash
    git clone https://github.com/ErwinLiYH/MiniPicBedMac.git
    cd MiniPicBedMac
    ```
3. Modify settings in `__init__.py`
    ```python
    # image saving directory
    # default: ~/mypicbed
    FILES_DIRECTORY = os.path.expanduser('~/mypicbed/')
    
    # server port, default: 20119
    PORT = 20119

    # copy behavior: MD to copy markdown code to refer the image
    # URL to copy URL of the image only
    # PATH to copy the image path
    # default: MD
    COPY_BEVAIOR = "MD"  # "MD", "URL" or "PATH"
    ```
4. Install
    ```bash
    pip install .
    ```


## Usage

1. Run PiBed
    ```bash
    python -m local_picbed_mac&
    ```
2. Copy a image
3. Click `MyPicbed` in status bar
4. Click `Save Image for Pastedboard`
5. Copy the image MD/URL/PATH to anywhere
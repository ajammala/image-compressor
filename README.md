
# Image Compressor

**Image Compressor** is a Python command-line tool designed to compress JPEG images in a given directory, utilizing multi-threading for faster processing. It allows you to specify the quality of the compression and the number of threads (workers) to use for parallel processing.

## Features

- Compress all JPEG images in a specified input directory.
- Output the compressed images to a specified output directory.
- Adjust the compression quality (default is 85).
- Use multi-threading to speed up the compression process.
- Simple and easy-to-use command-line interface.

## Requirements

- Python 3.x
- Pillow (Python Imaging Library)

## Installation

1. Clone or download this repository to your local machine:

   ```bash
   git clone https://github.com/ajammala/image_compressor.git
   cd image_compressor
   ```

2. Install the tool using `pip`:

   ```bash
   pip install .
   ```

   This will install the `compress-images` command-line tool.

## Usage

Once installed, you can use the tool directly from the command line.

```bash
compress-images <input_directory> <output_directory> [--quality QUALITY] [--workers WORKERS]
```

### Arguments:

- `<input_directory>`: Path to the input directory containing JPEG images to compress.
- `<output_directory>`: Path to the output directory where compressed images will be saved.

### Optional Arguments:

- `--quality`: Set the compression quality (integer between 0 and 100, default is 85). Higher values result in better quality but larger file sizes.
- `--workers`: Set the number of worker threads to use for parallel processing (default is 4). Increase this for faster processing on systems with more CPU cores.

### Example:

```bash
compress-images /path/to/input /path/to/output --quality 75 --workers 8
```

This command compresses JPEG images in `/path/to/input`, saves the compressed images in `/path/to/output`, with a compression quality of 75, and uses 8 threads for parallel processing.

### Output:

After running the command, you will see output like:

```
Compressed and saved image1.jpg successfully.
Compressed and saved image2.jpg successfully.

=== Summary ===
Number of files processed: 2
Total size before compression: 15.24 MB
Total size after compression: 9.67 MB
Total space saved: 5.57 MB
```

## Uninstallation

To uninstall the tool, run:

```bash
pip uninstall image_compressor
```

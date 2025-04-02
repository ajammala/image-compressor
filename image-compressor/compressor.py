import os
from PIL import Image
import concurrent.futures
import threading

# Lock for safely updating shared resources in threads
print_lock = threading.Lock()

def get_total_size(directory):
    """Calculate the total size (in bytes) of all JPEG files in the directory."""
    total_size = 0
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.jpg', '.jpeg')):
            file_path = os.path.join(directory, filename)
            total_size += os.path.getsize(file_path)
    return total_size

def compress_image(input_path, output_path, quality=85):
    """Compress a single image and save it to the output path."""
    try:
        with Image.open(input_path) as img:
            # Save the image with compression
            img.save(output_path, 'JPEG', quality=quality)

        with print_lock:
            print(f"Compressed and saved {os.path.basename(input_path)} successfully.")
    except Exception as e:
        with print_lock:
            print(f"Error processing {os.path.basename(input_path)}: {e}")

def compress_jpegs(input_dir, output_dir, quality=85, max_workers=4):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Gather information before processing
    initial_total_size = get_total_size(input_dir)

    # Collect JPEG files from the input directory
    files_to_compress = [f for f in os.listdir(input_dir) if f.lower().endswith(('.jpg', '.jpeg'))]

    # Multi-threading using ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for filename in files_to_compress:
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            futures.append(executor.submit(compress_image, input_path, output_path, quality))
        
        # Wait for all threads to complete
        concurrent.futures.wait(futures)
    
    # Get total size after conversion
    final_total_size = get_total_size(output_dir)

    # Logging summary
    print(f"\n=== Summary ===")
    print(f"Number of files processed: {len(files_to_compress)}")
    print(f"Total size before compression: {initial_total_size / (1024 * 1024):.2f} MB")
    print(f"Total size after compression: {final_total_size / (1024 * 1024):.2f} MB")
    print(f"Total space saved: {(initial_total_size - final_total_size) / (1024 * 1024):.2f} MB")

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Compress JPEG images.")
    parser.add_argument('input_directory', help="Path to the input directory containing JPEG files")
    parser.add_argument('output_directory', help="Path to the output directory to save compressed images")
    parser.add_argument('--quality', type=int, default=85, help="Compression quality (default: 85)")
    parser.add_argument('--workers', type=int, default=4, help="Number of threads to use for compression (default: 4)")

    args = parser.parse_args()

    compress_jpegs(args.input_directory, args.output_directory, args.quality, args.workers)

if __name__ == "__main__":
    main()

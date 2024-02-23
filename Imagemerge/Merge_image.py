from PIL import Image
import os


def merge_images_horizontally(output_file):
    # Get the directory where the script is located
    folder_path = os.path.dirname(os.path.abspath(__file__))

    # Find all PNG images in the directory
    images = [Image.open(os.path.join(folder_path, file)) for file in os.listdir(folder_path) if file.endswith('.png')]

    if not images:
        raise ValueError("No PNG images found in the folder")

    # Calculate the total width and maximum height
    total_width = sum(image.width for image in images)
    max_height = max(image.height for image in images)

    # Create a new image to merge the found images
    merged_image = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for image in images:
        # Paste each image side by side
        merged_image.paste(image, (x_offset, 0))
        x_offset += image.width

    # Save the merged image to the specified output file
    merged_image.save(output_file)


# Example usage
output_file = 'merged_image.png'  # Name of the output file
merge_images_horizontally(output_file)

import numpy as np
from PIL import Image

def save_array_as_png(array, filename):
    """
    Convert 2D numpy array to PNG image and save to current directory.
    
    Args:
        array: 2D numpy array
        filename: Output PNG filename
    """
    if array.ndim != 2:
        raise ValueError("Array must be 2-dimensional")
    
    # Convert to uint8 if needed
    if array.dtype != np.uint8:
        array = ((array - array.min()) / (array.max() - array.min()) * 255).astype(np.uint8)
    
    image = Image.fromarray(array, mode='L')
    image.save(filename, 'PNG')

# Example usage
if __name__ == "__main__":
    # Create sample 2D array
    data = np.random.rand(100, 100) * 255
    save_array_as_png(data, "output.png")

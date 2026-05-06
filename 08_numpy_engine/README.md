# NumPy Image Engine

A command-line tool developed to perform low-level image manipulation using tensor operations. Instead of relying on high-level "black box" filters, this project implements image processing logic directly through matrix mathematics and NumPy vectorization.

## Core Learning & Logic

### 1. Image Representation as Tensors
I learned that digital images are essentially 3D NumPy arrays (Height x Width x Channels). Manipulating an image is simply a matter of performing linear algebra or slicing operations on these multi-dimensional arrays.

### 2. Resolution Downsampling (Slicing)
Instead of using standard interpolation, I implemented compression via **Step Slicing**. By selecting every $n^{th}$ pixel (e.g., `array[::2, ::2]`), the image dimensions are reduced with $O(1)$ complexity, demonstrating how data can be sampled without loops.

### 3. Luminance & Grayscale Conversion
I implemented the standard weighted average formula for luminance:
$$Y = 0.299R + 0.587G + 0.114B$$
This involved collapsing the 3rd dimension (RGB) into a 2D intensity matrix while preserving perceived brightness.

### 4. Manual Color Grading
By targeting specific indices in the color channel axis (Axis 2), I developed a custom "boost" logic. This involves:
*   Adding/Subtracting constants from specific channels.
*   Using `numpy.clip` to ensure values stay within the valid `[0, 255]` range, preventing data overflow.

## Technical Stack
*   **NumPy:** For vectorized matrix operations and memory management.
*   **Matplotlib:** For image I/O and visualizing mathematical results.
*   **Pillow (PIL):** Used for canvas management and final image padding for side-by-side comparisons.

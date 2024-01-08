# Avatar generator



![Image 1](/path/to/image1.jpg){: width="100px" height="100px"}
![Image 2](/path/to/image2.jpg){: width="100px" height="100px"}
![Image 3](/path/to/image3.jpg){: width="100px" height="100px"}


This script creates avatars of various sizes using random matrix generation and visualization through the PIL library.

## How to use

1. Install the necessary dependencies:

     ```bash
     pip install Pillow
     ```

2. Run the `main.py` script specifying the `sizes` and `number` parameters to create avatars:

     ```bash
     python main.py
     ```

    Where:
    - `sizes`: size of generated avatars (integer or range)
    - `number`: number of avatars for each size

## Example

```python
sizes = 5       # 3, 8 to generate avatars many other sizes 
number = 10

main(sizes, number)
```

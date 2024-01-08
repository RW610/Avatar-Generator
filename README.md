# Avatar generator

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
sizes = 5  # 3, 7 to generate avatars many other sizes 
number = 10

main(sizes, number)
```

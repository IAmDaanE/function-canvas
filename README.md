# Function Canvas

Visualize any mathematic function onto a canvas. Written in python with the pygame library.

## Getting Started

### Getting the Source

This project is [hosted on GitHub](https://github.com/IAmDaanE/function-canvas). You can download the zip or clone this project directly using this command:

```
git clone git@github.com:IAmDaanE/function-canvas.git
```

### Running the Program

Requirements: You must have Python 3.6 - 3.13.
1. Clone the repository or download the zip and unpack it to your directory of choice.
2. Navigate to that directory in a terminal.
3. In a venv or the global python version install the needed libraries.
    ```
    pip install -r requirements.txt
    ```
4. Run the program.
    ```
    python function_canvas.py
    ```

### Different Function

There are some prewritten functions but you can of course add your own. To use another one go to this part in the python file:
```python
if x <= WINDOW_WIDTH / 2:
        sqrt_graph()
        x += x_jump
```
Replace sqrt_graph() with oscillator(), chaos(), parabola() or heartbeat() or write your own above and replace sqrt_graph() with the new function.

## License

This project is open-source and available under the MIT License.
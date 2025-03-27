# Shift-Clicker Autoclicker for Ren'Py Games

This Python script provides an autoclicker functionality primarily designed for Ren'Py visual novels, where manual clicking through dialogue can be tiring, and the built-in Ctrl skip feature is often too fast for comfortable reading. Beyond Ren'Py, it can be adapted for any application requiring automated mouse clicks. The autoclicker uses the Shift key to trigger clicking by default, with configurable options for enabling, disabling, adjusting click speed, and exiting safely.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
    - [All Users](for-all-users)
    - [Linux (Virtual Enviroment is Recommended)](for-linux-users-recommended-use-a-virtual-environment)
- [Alternative Way to Run on Linux](#alternative-way-to-run-on-linux)
- [Usage](#usage)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Warning](#warning)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Enable/Disable**: Toggle the autoclicker on with the **Home** key and off with the **End** key.
- **Click Trigger**: Hold the **Shift** key to start automatic clicking (when enabled).
- **Adjustable Click Delay**: Use the **Tilde (`)** key to enter a new delay (e.g., 0.5 seconds), confirmed with the **Insert** key.
- **Delay Display**: Press the **Insert** key (outside input mode) to view the current click delay.
- **Safe Exit**: Press the **Delete** key and confirm with 'y' or cancel with 'n' to exit the program.
- **Low System Impact**: Minimal delay in the click loop prevents overloading your system.

## Requirements

To run this script, you'll need the following:

- **Python 3.x**: The script is written in Python 3 and requires a compatible interpreter.
- **pyautogui**: A library for simulating mouse clicks.
- **pynput**: A library for handling global keyboard events.
- **Operating System**: Optimized for Unix-like systems (e.g., Ubuntu, Linux) with terminal echo control, but it also runs on Windows (without echo disabling).

Below is an updated "Installation" section for your `README.md` file that includes recommended instructions for Linux users to set up the autoclicker script using a Python virtual environment. These steps ensure that dependencies are isolated, preventing conflicts with other Python projects on your system.

## Installation

Follow these steps to set up the autoclicker:

### For All Users

1. **Install Python**: Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/) or use a package manager like `apt` on Linux (`sudo apt install python3`).

2. **Install Dependencies**: Use `pip` to install the required libraries. Open a terminal or command prompt and run:

   ```
   pip install pyautogui pynput
   ```

3. **Download the Script**: Save the script as `shift_clicker.py` (or download it from this repository once uploaded).

### For Linux Users (Recommended: Use a Virtual Environment)

It’s highly recommended to use a Python virtual environment when setting up this project on Linux. A virtual environment isolates the project’s dependencies from your system-wide Python installation, avoiding potential conflicts with other projects.

Here are the steps:

1. **Install Python 3**: Ensure Python 3 is installed on your system. Check by running:

   ```
   python3 --version
   ```

   If it’s not installed, install it using your distribution’s package manager. For example, on Ubuntu:

   ```
   sudo apt update
   sudo apt install python3 python3-venv
   ```

2. **Create a Virtual Environment**: Navigate to your project directory and create a virtual environment:

   ```
   python3 -m venv venv
   ```

   This creates a directory named `venv` in your project folder, which contains the virtual environment.

3. **Activate the Virtual Environment**: Activate the virtual environment before installing dependencies or running the script:

   ```
   source venv/bin/activate
   ```

   Your terminal prompt will change (e.g., it might prepend `(venv)`), indicating you’re now working inside the virtual environment.

4. **Install Dependencies**: With the virtual environment activated, install the required packages:

   ```
   pip install pyautogui pynput
   ```

5. **Run the Script**: While still in the virtual environment, run the script:

   ```
   python shift_clicker.py
   ```

6. **Deactivate the Virtual Environment**: When you’re finished, deactivate the virtual environment:

   ```
   deactivate
   ```

Using a virtual environment keeps your project’s dependencies separate and manageable, making it easier to maintain and troubleshoot.

## Alternative Way to Run on Linux

For Linux users, the repository includes a `run.sh` shell script that offers a convenient way to run the autoclicker. This script activates a virtual environment and executes the `shift_clicker.py` Python script in one step, simplifying the process compared to manually activating the environment and running the script.

### Provided `run.sh` Script

Here’s the content of the `run.sh` script included in the repository:

```
#!/bin/bash
VENV_PATH="$HOME/venv"
PYTHON="$VENV_PATH/bin/python"
SCRIPT_PATH="$(dirname "$0")/shift_clicker.py"

if [ ! -f "$PYTHON" ]; then
    echo "Error: Python interpreter not found in $PYTHON"
    exit 1
fi

if [ ! -f "$SCRIPT_PATH" ]; then
    echo "Error: Python script not found at $SCRIPT_PATH"
    exit 1
fi

"$PYTHON" "$SCRIPT_PATH"
```

### Steps to Use `run.sh`

1. **Ensure the Virtual Environment is Set Up**:
   - Before using `run.sh`, you must have a virtual environment with the required dependencies (`pyautogui` and `pynput`) installed. Refer to the [Installation](#installation) section of this README for instructions on creating and setting up the virtual environment.
   - By default, the script assumes the virtual environment is located at `$HOME/venv`.

2. **Modify `run.sh` if Necessary**:
   - The script uses two key variables:
     - `VENV_PATH="$HOME/venv"`: The path to your virtual environment.
     - `SCRIPT_PATH="$(dirname "$0")/shift_clicker.py"`: The path to the `shift_clicker.py` script, assumed to be in the same directory as `run.sh`.
   - If your virtual environment or `shift_clicker.py` script is in a different location, update these variables in `run.sh`. For example:
     - If your virtual environment is in the project folder as `venv`, change it to:
       ```
       VENV_PATH="$(dirname "$0")/venv"
       ```
     - If your script is named differently or located elsewhere, adjust `SCRIPT_PATH` accordingly, e.g., `SCRIPT_PATH="/path/to/shift_clicker.py"`.

3. **Make `run.sh` Executable**:
   - Run this command in your terminal to grant execute permissions:
     ```
     chmod +x run.sh
     ```

4. **Run the Script**:
   - Execute the script with:
     ```
     ./run.sh
     ```
   - The script will check for the Python interpreter and the `shift_clicker.py` file, then run the autoclicker if both are found.

### Project Structure

To help you understand how the script interacts with the project files, here’s the expected structure based on the default `run.sh` settings:

```
home/
├── venv/                   # Virtual environment directory (default: $HOME/venv)
│   ├── bin/
│   │   └── python          # Python interpreter in the virtual environment
│   └── ...                 # Other virtual environment files
└── project-folder/         # Your project directory
    ├── shift_clicker.py    # The main Python script
    └── run.sh              # Shell script to run the autoclicker
```

- **`venv/`**: The virtual environment directory, located at `$HOME/venv` by default, containing the Python interpreter and dependencies.
- **`shift_clicker.py`**: The autoclicker Python script, located in the same directory as `run.sh`.
- **`run.sh`**: The shell script that ties everything together.

### Important Notes

- **Path Customization**: If your virtual environment isn’t at `$HOME/venv` or if `shift_clicker.py` is in a different location, you *must* modify the `VENV_PATH` and `SCRIPT_PATH` variables in `run.sh` to match your setup. Failing to do so will result in errors like "Python interpreter not found" or "Python script not found."
- **Error Handling**: The script includes basic checks to ensure the Python interpreter and script file exist before running. If there’s an issue, it will display an error message and exit.
- **Dependencies**: Ensure the virtual environment has the necessary Python packages installed (`pyautogui` and `pynput`). See the [Installation](#installation) section for details.

This method streamlines running the autoclicker on Linux, making it ideal for users who want a quick, automated way to launch the script without manually managing the virtual environment.

## Usage

Here’s how to use the autoclicker:

1. **Run the Script**: Open a terminal or command prompt, navigate to the script’s directory, and execute:

   ```
   python shift_clicker.py
   ```
   or
   ```
   python3 shift_clicker.py
   ```

3. **Understand the Interface**: On startup, the script displays a welcome message and key bindings:
   ```
   Welcome to Shift-Clicker Program!
   | Home: Enable | End: Disable | Insert: Delay Value | Backtick: Edit | Delete: Exit |
   ```

4. **Enable the Autoclicker**: Press the **Home** key to activate it. You’ll see "Script enabled" in the terminal.

5. **Position the Cursor**: Move your mouse cursor to the desired click location (e.g., the "Next" button in Ren'Py).

6. **Start Clicking**: Hold the **Shift** key to begin automatic clicking at the current cursor position.

7. **Adjust Click Delay**:
   - Press the **Tilde (`)** key to enter input mode.
   - Type a delay in seconds (e.g., `0.5` for half a second).
   - Press the **Insert** key to confirm. The new delay will be displayed (e.g., "Delay updated to 0.5 seconds").
   - Note: The default delay is 0.4 seconds.

8. **Check Current Delay**: Press the **Insert** key (when not in input mode) to see the current delay (e.g., "Current delay: 0.4 seconds").

9. **Disable Without Exiting**: Press the **End** key to stop the autoclicker without closing the script. You’ll see "Script disabled."

10. **Exit the Program**:
   - Press the **Delete** key to initiate exit.
   - Confirm by pressing `y` (program terminates) or cancel with `n` (returns to normal operation).

### Note for Ren'Py Users

- **Setup**: Place the mouse cursor over the "Next" button or wherever you want to click in the Ren'Py game window.
- **Usage**: Enable the script with **Home**, then hold **Shift** to auto-click through dialogue or choices.
- **Speed**: Adjust the delay (e.g., 0.5 or 1.0 seconds) to match your reading speed for a comfortable experience.

## Customization

You can tweak the script to suit your needs:

- **Change the Click Trigger**: By default, the **Shift** key triggers clicking. To use a different key:
  - Open `shift_clicker.py` in a text editor.
  - Locate the `on_press` function and find `if key == keyboard.Key.shift`.
  - Replace `keyboard.Key.shift` with another key, such as `keyboard.Key.ctrl_l` (left Ctrl) or `keyboard.Key.space`. See the [pynput documentation](https://pynput.readthedocs.io/en/latest/keyboard.html#reference) for key names.

- **Modify Other Key Bindings**: Adjust keys like **Home**, **End**, **Tilde**, **Insert**, or **Delete** by changing the corresponding `keyboard.Key` values in the `on_press` function.

- **Default Delay**: Change the initial `click_delay = 0.4` at the top of the script to your preferred value (in seconds).

## Troubleshooting

Here are solutions to common issues:

- **Key Presses Not Detected**:
  - Ensure the script is running (check the terminal for output).
  - On some systems, try giving focus to the terminal window, though `pynput` typically captures keys globally.

- **Typed Characters Appear (Windows)**:
  - On Windows, terminal echo isn’t disabled, so you may see characters when typing delays. This is normal and doesn’t affect functionality.

- **Clicking Too Fast or Slow**:
  - Adjust the delay using the **Tilde** and **Insert** keys (e.g., `0.1` for faster, `1.0` for slower).

- **Script Won’t Exit**:
  - Use **Delete** followed by `y` to exit cleanly. Alternatively, press `Ctrl+C` in the terminal to force quit (echo will be restored on Unix-like systems).

## Warning

- **Responsible Use**: Autoclickers can violate the terms of service of some games or software. Use this script responsibly and only where permitted (e.g., for personal convenience in Ren'Py games).

## Contributing

- Want to improve the script? Feel free to fork this repository and submit pull requests with enhancements (e.g., GUI support, additional key options).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

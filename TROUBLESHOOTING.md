# Modal Labs - Troubleshooting Notes

## Common Issues

### Error: `zsh: command not found: modal`

This error occurs when the `modal` command is not available in your PATH. Here are solutions to try:

#### 1. Use `python3 -m modal` instead:
```bash
python3 -m modal run get_started.py
```

#### 2. Check if Modal was installed correctly:
```bash
pip3 show modal
```

#### 3. If using a virtual environment, make sure it's activated:
```bash
# If you have a virtual environment, activate it first
source venv/bin/activate  # or whatever your venv is called
# Then try the modal command
modal run get_started.py
```

#### 4. Check your Python/pip installation:
```bash
which python3
which pip3
```

#### 5. Try reinstalling Modal:
```bash
pip3 uninstall modal
pip3 install modal
```

#### 6. If you're using Poetry or pipenv:
```bash
# For Poetry
poetry run modal run get_started.py

# For pipenv
pipenv run modal run get_started.py
```

**Note:** The most common solution is using `python3 -m modal` instead of just `modal`.
# FocusFlow

A lightweight command-line task planner built with Python. Use it to organize study sessions, coding tasks, and personal projects.

## Features

- Add, list, complete, and delete tasks
- Stores tasks locally in a JSON file
- Shows total, completed, and pending task counts
- Uses only the Python standard library at runtime
- Includes automated tests

## Requirements

- Python 3.10 or newer

## Quick start

Clone or download this repository, open a terminal in its folder, and run:

```bash
python focusflow.py add "Learn Python functions"
python focusflow.py add "Build my first GitHub project"
python focusflow.py list
python focusflow.py done 1
python focusflow.py stats
python focusflow.py delete 2
```

On Windows, use `py` instead of `python` if that is how Python is configured on your computer.

## Run tests

Install pytest:

```bash
python -m pip install pytest
python -m pytest
```

## Data storage

Tasks are saved in `~/.focusflow_tasks.json` (your home directory). The project does not send data to any server.

## Roadmap

- [ ] Add task priorities and due dates
- [ ] Add categories such as university, coding, and personal
- [ ] Add CSV export
- [ ] Build a small graphical interface

## Contributing

Ideas, bug reports, and pull requests are welcome. Please open an issue to discuss larger changes.

## License

MIT

import os
from pathlib import Path

list_of_file = [
    ".github/worflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/logger/__init__.py",
    "src/logger/logger_method.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/exception/__init__.py",
    "src/exception/Exception.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/unit/test_unit.py",
    "tests/integration/__init__.py",
    "tests/integration/test_int.py",
    "pyproject.toml",
    "setup.py",
    "setup.cfg",
    "requirements.txt",
    "requirements_dev.txt",
    "init_setup.sh",
    "tox.ini"
]

for file_path in list_of_file:
    file_path = Path(file_path)
    print(f"file_path: {file_path}\n")
    dir_name = os.path.dirname(file_path)
    # new method using Path and pathlib and more robust
    # Learned from the GPT
    if file_path.parent != Path("."):
        # Mistake 1: This file_path.parent is property and not a function
        # ( not to be called as --> file.parent())
        file_path.parent.mkdir(parents=True, exist_ok=True)
    else:
        print(f"\nfile_path_parent: {file_path.parent}\n")

    if not file_path.exists() or file_path.stat().st_size == 0:
        file_path.touch()

""" old and less robust method
    Self written
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)

    with open(file_path, 'w') as f:
        pass
"""

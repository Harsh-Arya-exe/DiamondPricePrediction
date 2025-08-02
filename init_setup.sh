echo [$(date)]: "Starting the init_setup file"

echo [$(date)]: "Making the python venv"

python -m venv .env

echo [$(date)]: "Activating the virtual environment"

source .env/Scripts/activate

echo [$(date)]: "Reading and Installing the dependencies"

pip install -r requirements_dev.txt

echo [$(date)]: "File ended and closing it"
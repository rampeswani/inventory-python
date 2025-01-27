echo "BUILD START"

# Update package manager and install PostgreSQL development libraries
apt-get update && apt-get install -y libpq-dev gcc

# Ensure pip and dependencies are installed
python3.10 -m ensurepip --upgrade
python3.10 -m pip install --upgrade pip
python3.10 -m pip install -r requirements.txt

# Collect static files
python3.10 manage.py collectstatic --noinput --clear

echo "BUILD END"

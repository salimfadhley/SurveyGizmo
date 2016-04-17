#! /bin/bash
virtualenv venv --python=`which python3.5` --prompt="(surveygizmo)" --clear --verbose
source venv/bin/activate
venv/bin/pip install -e src

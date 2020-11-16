
# Setup slave nodes
# Copy this file to each slave
cpall ${PROJ_ROOT}/setup-slaves.sh /setup-slaves.sh
# Check if the files are there, except for node1
doall "ls /setup-slaves.sh"
# Setup the salve nodes using the setup script
doall -t 300 "bash /setup-slaves.sh"

# Check the setup integrity
doall "cmake --version"
doall "which cmake"
doall 'python3 -c "import xgboost; print(xgboost.__version__)"'

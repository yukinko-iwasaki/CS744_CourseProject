echo "source /workspace/CS744_CourseProject/xgboost.config.sh" >> ~/.bashrc

# Setup slave nodes
# Copy this file to each slave
cpall ${PROJ_ROOT}/setup-slaves.sh /setup-slaves.sh
# Check if the files are there, except for node1
doall "ls /setup-slaves.sh"
# Setup the salve nodes using the setup script
doall "bash /setup-slaves.sh"

# Check the setup integrity
doall "cmake --version"
doall "which cmake"
doall 'python3 -c "import xgboost; print(xgboost.__version__)"'

# Startup hadoop and yarn
# See also: https://www.linode.com/docs/guides/how-to-install-and-set-up-hadoop-cluster/
startall

# Only start yarn
# startyarn
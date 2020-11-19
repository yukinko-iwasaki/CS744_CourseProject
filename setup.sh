
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

# Startup hadoop

# Startup yarn

# YARN_RESOURCEMANAGER_USER=root HADOOP_SECURE_DN_USER=yarn YARN_NODEMANAGER_USER=root RMHOSTS="node1 node2 node3" 
# YARN_RESOURCEMANAGER_USER=root HADOOP_SECURE_DN_USER=yarn YARN_NODEMANAGER_USER=root RMHOSTS="node1 node2 node3" 
alias startyarn='${HADOOP_EXEC_ROOT}/start-yarn.sh'
alias stopyarn='${HADOOP_EXEC_ROOT}/stop-yarn.sh'
alias startall='${HADOOP_EXEC_ROOT}/start-all.sh'
alias stopall='${HADOOP_EXEC_ROOT}/stop-all.sh'
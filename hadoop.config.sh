# Path variables

export HADOOP_HOME=$HOME/hadoop-3.1.4
export HADOOP_BIN_ROOT="$HADOOP_HOME/bin"
export HADOOP_EXEC_ROOT="$HADOOP_HOME/sbin"
export JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"

export PATH=$PATH:${HADOOP_BIN_ROOT}
export PATH=$PATH:${HADOOP_EXEC_ROOT}
export PATH=$PATH:${JAVA_HOME}/bin

# Simple commands to start hdfs and yarn

YARN_FLAGS='YARN_RESOURCEMANAGER_USER=root HDFS_DATANODE_SECURE_USER=root YARN_NODEMANAGER_USER=root RMHOSTS="node1 node2 node3"'

HDFS_FLAGS="HDFS_DATANODE_USER=root HDFS_DATANODE_SECURE_USER=root HDFS_NAMENODE_USER=root HDFS_SECONDARYNAMENODE_USER=root"

alias startyarn='${HADOOP_EXEC_ROOT}/start-yarn.sh'
alias stopyarn='${HADOOP_EXEC_ROOT}/stop-yarn.sh'

alias startall='${HADOOP_EXEC_ROOT}/start-all.sh'
alias stopall='${HADOOP_EXEC_ROOT}/stop-all.sh'

# alias startyarn='${YARN_FLAGS} ${HADOOP_EXEC_ROOT}/start-yarn.sh'
# alias stopyarn='${YARN_FLAGS} ${HADOOP_EXEC_ROOT}/stop-yarn.sh'
# alias startall='${HDFS_FLAGS} ${HADOOP_EXEC_ROOT}/start-all.sh'
# alias stopall='${HDFS_FLAGS} ${HADOOP_EXEC_ROOT}/stop-all.sh'
export PROJ_ROOT="/workspace/CS744_CourseProject"
export CMAKE_ROOT="/usr/local/lib/python3.6/dist-packages/cmake/data/bin"
export PATH="${CMAKE_ROOT}:${PATH}"

alias doall='parallel-ssh -H "node0 node1 node2 node3" -P -t 300000 '
alias cpall='parallel-scp -H "node1 node2 node3"'

alias echoall='doall echo Hello World'
alias cp-proj='cpall -r ${PROJ_ROOT} ${PROJ_ROOT}'

source "$PROJ_ROOT/hadoop.config.sh"
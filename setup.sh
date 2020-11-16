# Install default python distribution of xgboost
doall "apt update"
doall "sudo apt install -y python3-pip"
doall -t 150 "pip3 install xgboost"

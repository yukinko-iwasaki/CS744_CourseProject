# Install default python distribution of xgboost
mkdir -p /workspace
sudo apt update
sudo apt install -y python3-pip
pip3 install cmake
pip3 install xgboost
pip3 install "dask[complete]"
pip3 install asyncssh
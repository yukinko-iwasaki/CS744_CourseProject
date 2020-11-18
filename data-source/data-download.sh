#=====================================================================
# Setup the dataset
#   Don't run the following commands if you don't have 1T storage.
#=====================================================================

# Install aria2
# https://ilouis.cn/practice/aria2.html

cd /tmp
wget https://github.com/q3aql/aria2-static-builds/releases/download/v1.35.0/aria2-1.35.0-linux-gnu-64bit-build1.tar.bz2
tar -jxvf aria2-1.35.0-linux-gnu-64bit-build1.tar.bz2
cd aria2-1.35.0-linux-gnu-64bit-build1
make install

sudo vi /etc/systemd/system/aria2c.service
systemctl enable aria2c
sudo systemctl start aria2c
sudo systemctl status aria2c


# Download data through aria2
# Don't run the following commands if you don't have 1T storage.

aria2c  --dir=/mydata \
        --max-concurrent-downloads=6  \
        --always-resume=true \
        --input-file download-paths.txt \
        --human-readable=true

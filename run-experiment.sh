
# Open a remote jupyter notebook
jupyter notebook --allow-root --port=9000 

# Local connection to the xgboost instance
ssh -f -N -L 9000:localhost:9000 xgboost

# Connect the dashboard
# Execute this when notebook client is setup and the dashbaord comes up
ssh -f -N -L 8797:localhost:8797 xgboost
# Repository for final project
# Run Flask
flask: flask --app server --debug run
# Test with curl
curl -X GET -i -w '\n' localhost:5000
#
# Run SCA: 
pip3 install pylint==2.11.1
pylint server.py



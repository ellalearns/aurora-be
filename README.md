# Aurora (Back-End)

This is the back-end implementation of the Aurora app.
My ALX foundations portfolio project.


## how to run locally


````git clone https://github.com/ellalearns/aurora-be.git````


move into the aurora-be directory


````cd aurora-be````


(optional) create virtual env


````python3 -m venv aurora````


(optional) activate virtual env


````source ./aurora/bin/activate````


rename .testenv to .env


````mv .testenv .env````


modify .env file if needed


change to .env sql user 


````source .env````


install required packages 


````pip install -r requirements.txt````


install aurora-be as a package using setup.py


````pip install .````


remove the build folder just created


````rm -rf build````


run the API 😊


````python3 ./api/v1/app.py````


## how to run entire Aurora on local machine

check out how to run the fe, be, and db.


run db first, then be, then fe.


😙 😙 😙


# DlvrMe-API

This is the backend code for the DlvrMe project the frontend of the mobile app can be found 
here: https://github.com/yassataiseer/DlvrMe-Mobile
### Tech Stack:
|Library/Framework| Purpose |
| ------ | ------ |
| Flask | Backend Api |
| MySQL | Database |
| Flutter| Frontend UI |


### Installation
Requires python 3
Requires Flutter
Android Studio
#### Mac& Linux(Rest-Api):
```sh
python3 app.py
```
#### Windows(Rest-Api):
``` sh
python app.py
```

## Building Database
DlvrMe runs on a MySQL databases
There is a need for two tables Users and Deliveries

#### User's Tables
The user's table will look like this:
|VALUE| TYPE  |
| ------ | ------ |
| Username | VARCHAR |
| Password | VARCHAR |

#### Deliveries Database
| VALUE  | TYPE |
| ------ | ------ |
| Username | VARCHAR |
| Address | VARCHAR |
| Latitude | FLOAT |
| Longitude | FLOAT |
| Item | VARCHAR |
| Price | FLOAT |
| User_info | VARCHAR |

#### How to Build:
First make Schema called dlvrme
Next run ``` models.py ```
In order to run you can either write in the file this line:
```py 
db.create_all()
 ```
OR run this terminal script:
```py

from models import db
db.create_all()
````

## Environment Variables
In order for the database to move smoothly environment variables must be generated.
Generate a folder called ``` .env ```
After this fill out the fold with this data:
```.env
HOST=YOUR_HOST
USERNAME=USERNAME
PASSWORD=DATABASE_PASSWD
DATABASE=DATABASE_NAME
```


### Open Sourcing Guidelines
Read ```CODE_OF_CONDUCT.md``` for proper rules
Instructions will come soon regarding what needs
to be improved.
Things to be done can be viewed at  ```CONTRIBUTING.md``` but do notify what
you will be doing before hand to prevent overwritten code.
Before opening a pull request make sure your code is tested, instructions 
in order to test your code can be found here.
Currently DlvrMe is not making new features rather improving current features.




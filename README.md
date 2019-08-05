# Direct upload
Sample project to show how direct upload can be done using Django.

### Requirements
- Python 2.7
- virtualenv
- PostgreSQL


### How to setup
- Clone the project
- Navigate to project's folder and run `mkvirtualenv direct-upload -r requirements.txt`
- Create the database with `createdb direct_upload`
- Migrate the database with `python manage.py migrate`
- Configure your AWS credentials exporting them in your terminal session:
    - `export AWS_ACCESS_KEY_ID='...'`
    - `export AWS_SECRET_ACCESS_KEY='...'`
    - `export AWS_STORAGE_BUCKET_NAME='...'`
- Run the server with `python manage.py runserver`

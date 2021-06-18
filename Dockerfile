FROM python
#NOT DONE YET
WORKDIR /DlvrMeAPI
#work directory

COPY requirements.txt requirements.txt
#copy requirements and install them
RUN pip3 install -r requirements.txt

COPY . .
#copy files in directory
EXPOSE 5000
#open 5000 port
CMD ["python3","./app.py"]
#run app
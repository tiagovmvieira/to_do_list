FROM python:3.9.7

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --noc-cache-dir -r requirements.txt

#copy
COPY . .

CMD ["python3", "manage.py", "runserver"]
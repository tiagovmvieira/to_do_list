FROM python:3.9.7

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

#copy source code
COPY . .

CMD ["python3", "manage.py", "runserver"]
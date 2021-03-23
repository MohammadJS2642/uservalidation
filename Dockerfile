FROM python:3.9

ENV PYTHONUNBUFFERED=1
WORKDIR /UserValidation


COPY requirements.txt .
RUN pip install -r requirements.txt


COPY . .

# RUN cd ./UserValidation/userValidation
# RUN python ./userValidation/manage.py makemigrations
# RUN python ./userValidation/manage.py migrate
# RUN python manage.py runserver 0.0.0.0:8000
# CMD [ "python ./userValidation/manage.py runserver 0.0.0.0:800"]
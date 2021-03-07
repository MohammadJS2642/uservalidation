FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /UserValidation
COPY requirements.txt .
RUN pip install -r requirements.txt
# WORKDIR /UserValidation/userValidation
COPY . .
WORKDIR /UserValidation/userValidation
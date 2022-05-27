# 
FROM python:3.10
# 
WORKDIR /code
# 
COPY ./app /code/app
# 
COPY ./requirements.txt /code/requirements.txt
# 
RUN /usr/local/bin/python -m pip install --upgrade pip
#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

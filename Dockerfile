FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && pip install --no-cache-dir 'fastapi[standard]'

COPY . .

EXPOSE 80
CMD [ "fastapi", "run", "./main.py", "--port", "80" ]

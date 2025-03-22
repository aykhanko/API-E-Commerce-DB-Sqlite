FROM python:3.12

WORKDIR /core

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY entrypoint.sh /entrypoint.sh  

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]

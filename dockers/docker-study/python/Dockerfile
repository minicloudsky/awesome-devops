FROM python:3
WORKDIR /usr/src/app
COPY . .
RUN  pip install --no-cache-dir -r requirements.txt \
        &&  cp -r ./ /root
WORKDIR /root
CMD ["python","main.py"]

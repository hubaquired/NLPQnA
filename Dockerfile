FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m deeppavlov install /usr/local/lib/python3.6/site-packages/deeppavlov/configs/squad/squad.json
RUN python -m deeppavlov download /usr/local/lib/python3.6/site-packages/deeppavlov/configs/squad/squad.json
COPY app.py ./

CMD ["python", "app.py"]

# CMD ["python", "-m", "deeppavlov", "interact", "/usr/local/lib/python3.6/site-packages/deeppavlov/configs/squad/squad.json"]

# RUN python -m deeppavlov interact squad.json

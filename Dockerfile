FROM python:3.6.4

ENV FLASK_APP app.py
ENV FLASK_ENV production
ENV FLASK_DEBUG 0

WORKDIR /app

ADD model.h5 /app/
ADD model.py /app/
ADD app.py /app/
ADD requirements.txt /app/

RUN pip install -r requirements.txt
ENTRYPOINT ["flask", "run"]
CMD ["--host=0.0.0.0", "--port=8084"]

EXPOSE 8084
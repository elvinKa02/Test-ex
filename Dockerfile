FROM python

WORKDIR /Test_EX

COPY . /Test_EX

RUN pip install eel

EXPOSE 8000

CMD python main.py

FROM python:3.7
ADD executor.py /home/executor.py
ADD requirements.txt ./
RUN pip install -r requirements.txt
ENTRYPOINT ["python","/home/executor.py"]
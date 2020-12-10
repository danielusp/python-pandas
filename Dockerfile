FROM amancevice/pandas:1.1.5-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install pymongo

ENTRYPOINT ["python"]
CMD ["default.py"]
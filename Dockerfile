FROM python:3.7

VOLUME /Users/raj/IdeaProjects/ml_task_address_parsing/data/
RUN git clone https://github.com/openvenues/libpostal && cd libpostal && ./bootstrap.sh && ./configure  --datadir="/libpostal_data/" &&  make && make install && ldconfig
RUN python -m pip install petl \
		pandas \
		wheel \
		postal
COPY main/ml_task.py data/Fire_Stations.csv data/Station_Locations.xml data/Station_Regions.csv ./
#COPY main/ml_task.py ./
CMD ["python", "ml_task.py"]
#COPY ml_task:ml_result.csv .

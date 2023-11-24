FROM mongo:7.0.3

COPY /data .

COPY start.sh /start.sh
#RUN chmod +x /start.sh

CMD /start.sh

#CMD mongoimport --host mongo --db data_wells --collection wells --type json --file /wells.json --jsonArray
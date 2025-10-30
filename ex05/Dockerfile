FROM openjdk:21-jdk-slim 

WORKDIR /var/currunt/app

COPY ./deploy/dockerserver-0.0.1-SNAPSHOT.jar ./application.jar

ENTRYPOINT ["java", "-jar", "./application.jar"]

CMD ["--server.port=3000"]
# Use the official OpenJDK image based on Alpine as the base image
FROM openjdk:17-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the Java file into the container
COPY HelloWorld.java .

# Compile the Java program
RUN javac HelloWorld.java

# Expose port 8001 so that the container can accept connections on that port
EXPOSE 8001

# Run the Java program
CMD ["java", "HelloWorld"]

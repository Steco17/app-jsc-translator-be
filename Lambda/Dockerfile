FROM amazonlinux:latest
ARG LAMBDA_NAME

# Set working directory
WORKDIR /app

# Copy code to container
COPY /${LAMBDA_NAME} /app 

# Install dependencies
RUN yum install -y python3 \
    && yum install -y python3-pip

# Install Python dependencies
RUN if [ -f "/app/requirements.txt" ]; then \
        pip3 install --no-cache-dir -r requirements.txt; \
    fi

# Run app
CMD ["python3", "app/app.handler"]
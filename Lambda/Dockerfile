FROM amazonlinux:latest
ARG LAMBDA_NAME

# Copy code to container
COPY /${LAMBDA_NAME} /app 
# - remove .lock file if copied
RUN if [ -f "/app/poetry.lock" ]; then rm -r /app/poetry.lock; fi 

# Set working directory
WORKDIR /app

# Install dependencies
RUN yum install -y python3 \
    && yum install -y python3-pip
RUN pip install poetry

# Install Python dependencies
RUN poetry config virtualenvs.create false && poetry install --no-interaction 
RUN poetry export --without-hashes --format=requirements.txt > requirements.txt
# RUN if [ -f "/app/requirements.txt" ]; then \
#         pip3 install --no-cache-dir -r requirements.txt; \
#     fi

# Run app
# CMD ["poetry", "run", "local"]      // poetry run local     -> translate.app:main
CMD ["poetry", "run", "lambda"]   // poetry run lambda    -> translate.app:handler
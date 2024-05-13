# FROM amazonlinux:latest
FROM public.ecr.aws/lambda/python:3.10
ARG LAMBDA_NAME

# Copy code to container
COPY /${LAMBDA_NAME} ${LAMBDA_TASK_ROOT} 
# - remove .lock file if copied
RUN if [ -f "${LAMBDA_TASK_ROOT}/poetry.lock" ]; then rm -r ${LAMBDA_TASK_ROOT}/poetry.lock; fi 
# setup for amazonlinux to be able to excute
RUN if [ -f "${LAMBDA_TASK_ROOT}/pyproject.toml" ]; then cp ${LAMBDA_TASK_ROOT}/pyproject.toml ${LAMBDA_TASK_ROOT}/poetry.toml ; fi 
# https://docs.aws.amazon.com/lambda/latest/dg/troubleshooting-deployment.html
RUN chmod 644 ${LAMBDA_TASK_ROOT}/poetry.toml

# Set working directory
WORKDIR ${LAMBDA_TASK_ROOT}

# # Install dependencies
# RUN yum install -y python3 \
#     && yum install -y python3-pip
RUN pip install poetry

# Install Python dependencies
RUN poetry config virtualenvs.create false --local && poetry install --no-interaction 
# RUN poetry export --without-hashes --format=requirements.txt > requirements.txt
# RUN if [ -f "/app/requirements.txt" ]; then \
#         pip3 install --no-cache-dir -r requirements.txt; \
#     fi

RUN poetry build

# Run app
# CMD ["poetry", "run", "local"]      // poetry run local     -> translate.app:main
# CMD ["poetry", "run", "lambda"]   // poetry run lambda    -> translate.app:handler
CMD [ "translate.run.lambda_handler" ]
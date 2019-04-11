FROM python:3.6-alpine

# Install Dependencies using Pipenv
WORKDIR /tmp/packages/
RUN pip install pipenv --no-cache-dir
COPY Pipfile* ./
RUN pipenv install --system
RUN pip uninstall pipenv --yes --no-cache-dir

WORKDIR /app/
COPY src/ ./

CMD ["python", "app.py"]
FROM apache/airflow:2.10.3

# Switch to airflow user BEFORE installing packages (Airflow requirement)
USER airflow

# Install pip packages correctly
RUN pip install --no-cache-dir requests pandas

# Switch to root ONLY to copy files
USER root
COPY pipelines /opt/airflow/pipelines
RUN chown -R airflow: /opt/airflow/pipelines

# Back to airflow
USER airflow

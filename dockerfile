# base image
FROM python:3.12

# workdir
WORKDIR /portfolio

# copy
COPY . /portfolio

# run
RUN pip install --no-cache-dir -r requirements.txt

# define variable
ENV APP_MODE=production

# port
EXPOSE 8501

# command
CMD ["streamlit", "run", "portfolio.py", "--server.port=8501"]

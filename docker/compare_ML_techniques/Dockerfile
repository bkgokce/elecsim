FROM python:3.6

COPY requirements.txt /
RUN pip install -r requirements.txt

#ADD . /app
COPY . /app

WORKDIR /app/run/market_forecasting_comparison/run/Compare_worlds/

ENV NAME World

# ENV PYTHONPATH "${PYTHONPATH}:/elecsim"
# VOLUME [ "my-vol" ]

# CMD ["python", "-m", "scoop", "run/validation-optimisation/run_price_fitter_investment/run_GA_price_fitter.py"]
# CMD ["python3", "run/market_forecasting_comparison/run/Compare_worlds/compare_by_ml_accuracy.py"]
CMD ["python3", "compare_by_ml_accuracy.py"]
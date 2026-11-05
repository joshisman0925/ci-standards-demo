FROM python:3.12-slim

WORKDIR /app
COPY calc/ calc/

RUN useradd --create-home appuser
USER appuser

CMD ["python", "-c", "from calc.fee import parking_fee; print(parking_fee(90))"]

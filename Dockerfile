FROM python:3.9-slim

RUN useradd -m appuser

WORKDIR /app

COPY pyproject.toml .
COPY README.md .
COPY meal_planner ./meal_planner

RUN pip install --no-cache-dir .

USER appuser

ENTRYPOINT ["meal-planner"]

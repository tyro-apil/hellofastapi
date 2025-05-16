# Dummy Calculator
A simple calculator app made using ***streamlit*** for UI and ***fastapi*** for serving endpoint.

## Instructions
### 1. Using docker compose
1. Install docker: [Official Page](https://docs.docker.com/engine/install/)
2. Run docker compose
    ```shell
    docker compose up -d
    ```

### 2. Running Locally
1. Install **uv** package manager: [Official Page](https://docs.astral.sh/uv/getting-started/installation/)
2. Create virtual environment and install packages
    ```shell
    uv sync
    ```
3. Start fastapi server
    ```shell
    uv run uvicorn fast_api:app --host 0.0.0.0 --port 8000
    ```
4. Start streamlit
    ```shell
    uv run streamlit run stream_lit.py --server.port=8501 --server.address=0.0.0.0
    ```

### 3. Running tests
1. Calculation tests
   ```shell
   uv run pytest -v test_calculator.py
   ```

2. Endpoint test
   ```shell
   uv run pytest -v test_endpoint.py
   ```
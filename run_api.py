# run_api.py
import uvicorn

if __name__ == "__main__":
    # Ejecuta la app en modo persistente
    uvicorn.run("src.serving:app", host="127.0.0.1", port=8000, reload=True)
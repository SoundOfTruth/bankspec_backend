Api для приложения bankspec требуемые библиотеки fastapi, psycopg2, requests, bs4, "uvicorn[standard]".
Запуск api производится через uvicorn main:app --reload --host 0.0.0.0 --port 10000, где 10000 это порт, который необходимо предварительно открыть.

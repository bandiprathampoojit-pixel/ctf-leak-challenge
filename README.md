# NoteKeeper API

A simple RESTful API for managing personal notes, built with Flask.

## Getting Started

```bash
pip install -r requirements.txt
python app.py
```

The server starts on `http://localhost:5000`.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET  | `/`       | API info       |
| GET  | `/health` | Health check   |
| GET  | `/notes`  | List notes     |
| POST | `/notes`  | Create a note  |

## License

MIT

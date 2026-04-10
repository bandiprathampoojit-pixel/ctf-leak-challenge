# NoteKeeper API

A simple RESTful API for managing personal notes, built with Flask.

## Getting Started

### Prerequisites
- Python 3.11+
- pip

### Installation

```bash
pip install -r requirements.txt
python app.py
```

The server starts on `http://localhost:5000`.

## API Endpoints

| Method | Endpoint | Description    |
|--------|----------|----------------|
| GET    | `/`       | API info        |
| GET    | `/health` | Health check    |
| GET    | `/notes`  | List all notes  |
| POST   | `/notes`  | Create a note   |

## Configuration

Copy `.env.example` to `.env` and fill in your values:

```
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///notes.db
```

## Deployment

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Contributing

Pull requests welcome. Please open an issue first to discuss changes.

## License

MIT

# MyEngine - Python Search Engine

A simple search engine built with Django that crawls websites and provides search functionality through both web UI and terminal interface.

## Features

- Web crawling and data extraction
- Inverted index for fast searching
- Clean web interface
- Terminal-based search option
- SQLite database storage

## Prerequisites

- Python 3.8+
- pip (Python package installer)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd SearchEngine_Python
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Web UI Version

1. **Navigate to the Django project**
   ```bash
   cd searchEngine
   ```

2. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

3. **Start the development server**
   ```bash
   python manage.py runserver
   ```

4. **Access the application**
   - Open your browser and go to: `http://127.0.0.1:8000/`
   - Use the search interface to find content

## Running the Terminal Version

1. **Navigate to the project root**
   ```bash
   cd terminalversion
   ```

2. **Run the terminal search**
   ```bash
   python main.py
   ```

3. **Follow the prompts**
   - Enter your search query when prompted
   - View results in the terminal

## Project Structure

```
SearchEngine_Python/
├── searchEngine/           # Django project
│   ├── home/              # Main app
│   │   ├── templates/     # HTML templates
│   │   ├── static/        # CSS/JS files
│   │   ├── views.py       # View functions
│   │   └── db.py          # Database operations
│   └── manage.py          # Django management script
├── terminalversion        # Terminal interface
      main.py
      db.py     
└── README.md             # This file
```

## Usage

### Web Interface
1. Enter search terms in the search box
2. Click "Search" to find relevant content
3. Click on results to view full content

### Terminal Interface
1. Run the terminal script
2. Type your search query
3. View results with URLs and snippets

## Database Setup

The application automatically creates necessary tables on first run. To populate with data:

1. Uncomment the data insertion loops in `views.py`
2. Run the server once to crawl and index websites
3. Comment the loops back to prevent re-crawling

## Troubleshooting

- **Port already in use**: Change port with `python manage.py runserver 8001`
- **Database errors**: Delete `db.sqlite3` and restart
- **Missing dependencies**: Run `pip install -r requirements.txt`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request
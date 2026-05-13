## Python Setup Cheat Sheet

### 1. Initialize Environment

```bash
python3 -m venv venv

```

### 2. Activate

* **Linux/Fedora:** `source venv/bin/activate`
* **Windows:** `.\venv\Scripts\activate`

### 3. Manage Packages

* **Install:** `pip install <package>`
* **Save List:** `pip freeze > requirements.txt`
* **Install List:** `pip install -r requirements.txt`

### 4. Exit

```bash
deactivate

```
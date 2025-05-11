🛍️ Flask Market

A simple web-based marketplace built with Flask, where users can register, log in, and buy or sell items. This project is perfect for those learning Flask and building full-stack Python web applications.

🚀 Features
🧑‍💼 User Registration & Login (with Flask-Login)
🔒 Password hashing (via Werkzeug)
📦 Add, Buy, and Sell Items
📜 Dynamic HTML with Jinja2 templating
💾 SQLite database (with SQLAlchemy ORM)
🎨 Bootstrap for responsive UI
📸 Demo
(Insert screenshot or GIF here once the app is running)

🛠️ Tech Stack
Python
Flask
SQLAlchemy
Flask-WTF
HTML/CSS (Bootstrap)
⚙️ Installation
git clone https://github.com/Sanjay-D-works/Flask_market.git
cd Flask_market
python3 -m venv venv
source venv/bin/activate  # On Windows use ⁠ venv\Scripts\activate ⁠
pip install -r requirements.txt
export FLASK_APP=shop.py
export FLASK_DEBUG=1
flask run


🗃️ Database Setup
Open a Python shell:

python
>>> from market import db

>>> db.create_all()

>>> exit()


📂 Project Structure

Flask_market/

├── shop.py
├── market.db
├── templates


📄 License
This project is open source under the MIT License.

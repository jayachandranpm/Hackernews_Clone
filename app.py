from flask import Flask, render_template, request, redirect, url_for, session, flash,  jsonify
from bs4 import BeautifulSoup
from flask_bcrypt import Bcrypt
import requests
import mysql.connector
from datetime import datetime, timedelta
import re
import secrets


app = Flask(__name__)
bcrypt = Bcrypt(app)


# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'hackernews'
}
'''
# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Check if user already exists in the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
        existing_user = cursor.fetchone()
        cursor.close()

        if existing_user:
            flash('User already registered. Please log in.')
            return redirect(url_for('login'))
        else:
            # Insert new user into the database
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, hashed_password))
            conn.commit()
            cursor.close()
            conn.close()
            flash('Account created successfully. Please log in.')
            return redirect(url_for('login'))
    return render_template('signup.html')


# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if user exists in the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()

        if user and bcrypt.check_password_hash(user[3], password):  # Assuming hashed password is in the fourth column
            session['username'] = username
            #flash('Logged in successfully!')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password. Please try again.')

    return render_template('login.html')


# Logout route
@app.route('/logout',methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    #flash('Logged out successfully!')
    return redirect(url_for('login'))
'''
# Function to parse HackerNews page and extract news items
def parse_hackernews_page(page_number):
    url = f"https://news.ycombinator.com/news?p={page_number}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_items = []

    # Use regular expressions to extract news items
    pattern = re.compile(r"\d+\.\s+(.*?)\s+\((.*?)\)\s+(\d+)\s+points\s+by\s+(.*?)\s+(\d+)\s+hours\s+ago\s+\|\s+hide\s+\|\s+(\d+)\s+comments")
    matches = pattern.findall(soup.get_text())

    # Iterate through matches and extract news items
    for match in matches:
        title, _, upvotes, _, hours_ago, comments = match
        hacker_news_url = f"https://news.ycombinator.com/news?p={page_number}"
        posted_on = datetime.now() - timedelta(hours=int(hours_ago))

        # Find the anchor tag containing the title
        title_anchor = soup.find('a', string=title)
        if title_anchor:
            url = title_anchor.get('href')
        else:
            url = None
        
        news_items.append((title.strip(), url, hacker_news_url.strip(), posted_on.strftime('%Y-%m-%d %H:%M:%S'), int(upvotes), int(comments)))

    return news_items

# Index route
@app.route('/')
def index():
    # Fetch news items from Hacker News
    news_items = []
    for page_number in range(1, 4):  # Crawling first three pages
        news_items.extend(parse_hackernews_page(page_number))

    return render_template('index.html', news_items=news_items)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(debug=True)

'''
def get_news_item_by_id(item_id):
    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Fetch the news item data
    cursor.execute("SELECT * FROM news_items WHERE id = %s", (item_id,))
    news_item = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    return news_item

@app.route('/comment/<int:item_id>', methods=['GET', 'POST'])
def comment(item_id):
    if 'username' not in session:
        flash('Please log in to add a comment.')
        return redirect(url_for('login'))

    if request.method == 'POST':
        comment_text = request.form['comment_text']
        username = session['username']

        # Fetch user ID from the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
        user_id = cursor.fetchone()[0]
        cursor.close()

        # Insert comment into the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user_comments (user_id, news_item_id, comment_text) VALUES (%s, %s, %s)",
                       (user_id, item_id, comment_text))
        conn.commit()
        cursor.close()
        conn.close()

        flash('Comment added successfully!')
        # Redirect to the comment page after adding the comment
        return redirect(url_for('comment', item_id=item_id))

    # Fetch the news item data (you'll need to implement this)
    news_item = get_news_item_by_id(item_id)
    return render_template('comment.html', news_item=news_item)
'''

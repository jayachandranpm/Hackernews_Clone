create database hackernews;
use hackernews;
CREATE TABLE IF NOT EXISTS news_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    url VARCHAR(255),
    hacker_news_url VARCHAR(255),
    posted_on DATETIME,
    upvotes INT,
    comments INT
);

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS user_interactions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            news_item_id INT,
            is_read BOOLEAN DEFAULT FALSE,
            is_deleted BOOLEAN DEFAULT FALSE,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (news_item_id) REFERENCES news_items(id)
            );
            
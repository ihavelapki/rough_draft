DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS roles;
DROP TABLE IF EXISTS groups;
DROP TABLE IF EXISTS schedule;

CREATE TABLE users (user_id INTEGER PRIMARY KEY AUTOINCREMENT
                    , user_email VARCHAR(100)
                    , user_name VARCHAR(100)
                    , user_avatar VARCHAR(100)
                    , process_date INTEGER
                    , process_dtime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                    , password_hash VARCHAR(100));

CREATE TABLE comments (comment_id INTEGER PRIMARY KEY AUTOINCREMENT
                    , process_dtime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                    , title TEXT NOT NULL
                    , content TEXT NOT NULL
                    , user_id INTEGER NOT NULL);
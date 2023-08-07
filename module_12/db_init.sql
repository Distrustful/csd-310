-- -----USER CREATION----- --
-- DROP USER IF EXISTS
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- CREATE whatabook_user
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- GRANT whatabook_user PRIVILAGES
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';

-- -----TABLE CREATION----- --
-- DROP TABLES IF EXISTS
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS store;

-- CREATE user TABLE
CREATE TABLE user(
    user_id        INT           NOT NULL        AUTO_INCREMENT,
    first_name     VARCHAR(75)   NOT NULL,
    last_name      VARCHAR(75)   NOT NULL,
    PRIMARY KEY(user_id)
); 

-- CREATE book TABLE
CREATE TABLE book (
    book_id       INT             NOT NULL       AUTO_INCREMENT,
    book_name     VARCHAR(200)    NOT NULL,
    author        VARCHAR(200)    NOT NULL,
    details       VARCHAR(500),
    PRIMARY KEY(book_id)
); 

-- CREATE wishlist TABLE
CREATE TABLE wishlist (
    wishlist_id    INT            NOT NULL        AUTO_INCREMENT,
    user_id        INT            NOT NULL,
    book_id        INT            NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_user 
    FOREIGN KEY(user_id) 
        REFERENCES user(user_id),
    CONSTRAINT fk_book 
    FOREIGN KEY(book_id) 
        REFERENCES book(book_id)
);  

-- CREATE store TABLE
CREATE TABLE store(
    store_id       INT            NOT NULL        AUTO_INCREMENT,
    locale         VARCHAR(500)   NOT NULL,
    PRIMARY KEY(store_id)
);

-- -----INSERT STATEMENTS----- --
-- INSET user RECORDS
INSERT INTO user(first_name, last_name)
    VALUES
        ('Taylor', 'Damron'),
        ('John', 'Doe'),
        ('Jane', 'Doe');

-- INSERT book RECORDS
INSERT INTO book(book_name, author, details)
    VALUES
        ('Maze Runner', 'James Dashner', 'First book in Maze Runner Series'),
        ('The Scorch Trials', 'James Dashner', 'Second book in Maze Runner Series'),
        ('The Death Cure', 'James Dashner', 'Third book in Maze Runner Series'),
        ('The Kill Order', 'James Dashner', 'Fourth book in Maze Runner Series'),
        ('The Maze Cutter', 'James Dashner', 'Fifth book in Maze Runner Series'),
        ('The Rule Of Three', 'Eric Walters', 'First book in The Rule Of Three Series'),
        ('The Fight For Power', 'Eric Walters', 'Second book in The Rule Of Three Series'),
        ('Will To Survive', 'Eric Walters', 'Third book in The Rule Of Three Series');

-- INSERT wishlist RECORDS
INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Taylor'),
        (SELECT book_id FROM book WHERE book_name = 'The Rule Of Three')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'John'),
        (SELECT book_id FROM book WHERE book_name = 'Maze Runner')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Jane'),
        (SELECT book_id FROM book WHERE book_name = 'The Maze Cutter')
    );

-- INSERT store RECORDS
INSERT INTO store(locale)
    VALUES('1234 Random ST, Farmington, UT 84025');

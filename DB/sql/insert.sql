-- Insert admin user
INSERT INTO users
        (email,         name,       surname,        password,       admin)
VALUES  ("admin@hoem",  "Admin",    "Admimenko",    "cs50password", 1);


-- other users INSERT Statement
INSERT INTO users
        (email,         name,       surname,        password)
VALUES  ("admin@hoem",  "Admin",    "Admimenko",    "cs50password");flask run
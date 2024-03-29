CREATE TABLE IF NOT EXISTS roles (
   role_id serial PRIMARY KEY,
   role_name VARCHAR (255) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
	user_id uuid PRIMARY KEY,
	username VARCHAR ( 255 ) UNIQUE NOT NULL,
	user_password VARCHAR ( 255 ) NOT NULL,
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
    last_login TIMESTAMP,
    disabled BOOLEAN
);

CREATE TABLE users_roles (
  user_id uuid NOT NULL,
  role_id INT NOT NULL,
  grant_date TIMESTAMP,
  PRIMARY KEY (user_id, role_id),
  FOREIGN KEY (role_id)
      REFERENCES roles (role_id),
  FOREIGN KEY (user_id)
      REFERENCES users (user_id)
);

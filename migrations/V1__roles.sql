CREATE TABLE IF NOT EXISTS scopes (
   scope_id serial PRIMARY KEY,
   scope_name VARCHAR (255) UNIQUE NOT NULL
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

CREATE TABLE user_scopes (
  user_id uuid NOT NULL,
  scope_id INT NOT NULL,
  grant_date TIMESTAMP,
  PRIMARY KEY (user_id, scope_id),
  FOREIGN KEY (scope_id)
      REFERENCES roles (scope_id),
  FOREIGN KEY (user_id)
      REFERENCES users (user_id)
);

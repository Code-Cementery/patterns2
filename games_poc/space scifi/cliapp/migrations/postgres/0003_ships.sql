CREATE TABLE IF NOT EXISTS ships (
    "sid" uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
    "created_at" timestamp NULL DEFAULT (now() AT TIME ZONE 'UTC'),

    "wid" uuid NULL,

    "pos_x" float NULL,
    "pos_y" float NULL,
    "pos_z" float NULL,

    "dir_x" float NULL,
    "dir_y" float NULL,
    "dir_z" float NULL,

    "captain" uuid REFERENCES users(uid)
);

-- Converting a database to utf8(utf8mb4, collate utf8mb4_unicode_ci)


ALTER DATABASE htbn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table CHANGE name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

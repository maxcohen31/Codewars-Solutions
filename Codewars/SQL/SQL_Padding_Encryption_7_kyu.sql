SELECT RPAD(encryption.md5, LENGTH(encryption.sha256), '1') AS md5,
LPAD(encryption.sha1, LENGTH(encryption.sha256), '0') AS sha1, 
encryption.sha256 AS sha256
FROM encryption
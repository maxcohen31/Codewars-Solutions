CREATE FUNCTION Increments(i integer) RETURNS integer AS $age$
BEGIN
  RETURN i + 1;
END;
$age$ LANGUAGE plpgsql;
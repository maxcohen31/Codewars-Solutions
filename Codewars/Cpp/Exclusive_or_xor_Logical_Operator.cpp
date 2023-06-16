bool xorf(bool a, bool b)
{
    return a^b;
}

bool xorf(bool a, bool b)
{
    if(a == !b) { return true; }
    return false;
}

bool xorf(bool a, bool b)
{
    if(!a != !b)
    {
      return true;
    }
    return false;
}

long pentagonal(long n) 
{   
    if(n <= 0)
    {
        return -1;
    }
    return ((5 * n * n) - (5 * n) + 2) / 2;
}

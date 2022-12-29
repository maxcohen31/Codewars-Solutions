class Arge
{
  public:
  static int nbYear(int p0, double percent, int aug, int p);
};

int Arge::nbYear(int p0, double percent, int aug, int p)
{
    int year {0};
    int new_p0 = p0;
    while (new_p0 < p)
    {
        new_p0 =  new_p0 + (new_p0 * (percent / 100)) + aug;
        year++;
    }
    return year;
}
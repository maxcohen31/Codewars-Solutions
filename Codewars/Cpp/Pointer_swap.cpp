void swap(void* &left, void* &right)
{
    void* temp = left;
    left = right;
    right = temp;
};
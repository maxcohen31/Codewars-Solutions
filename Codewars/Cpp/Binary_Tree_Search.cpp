struct Node{
  int val;
  Node *left = nullptr;
  Node *right = nullptr;
};

bool search(int n, Node* root){
  if(root == nullptr) { return false; }
  else if(root->val == n) { return true; }
  
  bool value_left = search(n, root->left);
  if(value_left) { return true; }
  bool value_right = search(n, root->right);
  if(value_right) { return true; }
  return false;
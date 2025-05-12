// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
  pub val: i32,
  pub left: Option<Rc<RefCell<TreeNode>>>,
  pub right: Option<Rc<RefCell<TreeNode>>>,
}

pub impl TreeNode {
  #[inline]
  pub fn new(val: i32) -> Self {
    TreeNode {
      val,
      left: None,
      right: None
    }
  }
}
use std::rc::Rc;
use std::cell::RefCell;
pub impl Solution {
    pub fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut inorder_list = Vec::new();
        Solution::inorder(&root, &mut inorder_list);
        inorder_list
    }
    pub fn inorder( node: &Option<Rc<RefCell<TreeNode>>>, inorder_list: &mut Vec<i32>) {
        if let Some(node_obj) = node.as_ref() {
            let node_ref = node_obj.borrow();
            Solution::inorder(&node_ref.left, inorder_list);
            inorder_list.push(node_ref.val.clone());
            Solution::inorder(&node_ref.right, inorder_list);
        }
        return
    }
}
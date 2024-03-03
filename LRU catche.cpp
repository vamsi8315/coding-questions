class LRUCache {
public:
    class Node{
        public:
        int key;
      int val;
      Node* next;
      Node* prev;
      Node(int key, int val){
          this->key=key;
          this->val=val;
      }
    };

    Node* head=new Node(-1,-1);
    Node* tail=new Node(-1,-1);
    int cap;
    unordered_map<int,Node*> m;
    
    LRUCache(int capacity) {
        cap=capacity;
        head->next=tail;
        tail->prev=head;
        
    }
    void addnode(Node* newnode){
        Node*temp= head->next;
        newnode->next=temp;
        temp->prev=newnode;
        newnode->prev=head;
        head->next=newnode;
    }
    void deletenode(Node* delnode){
        Node* p=delnode->prev;
        Node* q=delnode->next;
        p->next=q;
        q->prev=p;
    }
    
    int get(int key) {
        if(m.find(key)!=m.end()){
            Node* res=m[key];
            int ans=res->val;
            m.erase(key);
            deletenode(res);
            addnode(res);
            m[key]=head->next;
            return ans;
        }
        return -1;

        
    }
    
    void put(int key, int value) {
        if(m.find(key)!=m.end()){
            Node* p=m[key];
            m.erase(key);
            deletenode(p);
        }
        if(m.size()==cap){
            m.erase(tail->prev->key);
            deletenode(tail->prev);
        }
        Node*qq=new Node(key,value);
        addnode(qq);
        m[key]=head->next;
        
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */

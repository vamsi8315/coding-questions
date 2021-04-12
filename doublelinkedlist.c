#include<stdio.h>
struct node {
    int data;
    struct node *next;
    struct node *prev;
}*head;

void insert(int ele){
    //struct node* temp=(struct node*)malloc(sizeof(struct node));
     struct node *temp;
     temp= (struct node*)malloc(sizeof(struct node));
    if(head==NULL){
        temp->next=NULL;
        temp->prev=NULL;
        temp->data=ele;
        head=temp;
        
        //printf("%d",head->data);
    }
    else{
        temp->data=ele;
        temp->next=head;
        temp->prev=NULL;
        head->prev=temp;
        head=temp;
        //printf("%d",head->data);
        
    }
}
void display(){
    struct node *current=head;
    struct node *last;
    if(head==NULL){
        printf("list is empty");
        
    }

    else{
        while(current!=NULL){
            printf("%d<-->",current->data);
            if(current->next==NULL){
                last=current;
            }
            current=current->next;
    
            
        }
        printf("\n");
         while(last!=NULL){
            printf("%d<-->",last->data);
            //if(current->next==NULL){
              //  last=current;
            //}
            last=last->prev;
    
            
        }
    }

    
}

int main(){
    insert(10);
    insert(20);
    insert(30);
    insert(40);
    display();
    //delete();
    //display();
}

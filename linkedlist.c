#include <stdio.h>
void insert(int );
void display();
void delete();
struct node {
	int data;
	struct node *next;
}*head;

int main()
{
void insert(int ele){
    
	struct node *temp;
	temp=(struct node *)malloc(sizeof(struct node));
	temp->data=ele;
	temp->next=head;
	head=temp;
}
insert(10);
insert(20);
insert(30);
display();
printf("\n");
delete();
display();
}
void delete(){
    if(head){
        struct node *temp=head;
        head=head->next;
        free(temp);
    }
}
void display(){
	struct node *p;
	p=head;
	while(p){
		printf("%d->",p->data);
		p=p->next;
	}
}

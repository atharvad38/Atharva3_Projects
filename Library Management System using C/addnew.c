#include<stdio.h>
extern void addnew(){
    FILE *fp;
    int n,i,a;
    struct book{
        char title[30];
        char author[30];
        char publication[30];
        int available;
        float price;
        char id[15];
        char bug[3];
        char erp[30];
    };
    struct book bk;
    fp=fopen("bookrecord.txt","a");
    if(fp==NULL){
        printf("File is not created\n");
        goto end;
    }
    printf("Enter no. of books you want to store :");
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        gets(bk.bug);
        printf("\nEnter title of book :");
        gets(bk.title);
        fprintf(fp,"%s\t",bk.title);
        printf("\nEnter name of author :");
        gets(bk.author);
        fprintf(fp,"%s\t",bk.author);
        printf("\nEnter publication of book :");
        gets(bk.publication);
        fprintf(fp,"%s\t",bk.publication);
        printf("Enter price of book :");
        scanf("%f",&bk.price);
        fprintf(fp,"%2f\t",bk.price);
        printf("Enter availability :");
        scanf("%d",&bk.available);
        fprintf(fp,"%d\t",bk.available);
        srand(time(0));
        a =rand();
        itoa(a,bk.id,10);
        fprintf(fp,"%s",bk.id);
        
        printf("\nYour book is successfully saved!!");
    }


    if(fp==NULL){
        end:
        printf("Going back to main page\n");

    }
    fclose(fp);

}
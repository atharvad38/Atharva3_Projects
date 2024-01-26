#include<stdio.h>
#include"returned.c"
#include<string.h>
extern void returned(char *ptr);
extern void Return(){
    char bug[2],ch,word[12],str[10000],*tmp;
    int i,j;
    FILE *fp;
    printf("Enter erp of student :");
    gets(bug);
    gets(word);
    fp = fopen("studentrecord.txt","r");
    i=0;
    do{
        ch = fgetc(fp);
        str[i]=ch;
        i++;

    }while(str[i]!='\n');
    tmp = strstr(str,word);
    if(tmp!=NULL){
        printf("You are eligibile to return the book.");
        returned(word);
    }
    else{
        printf("You are not eligible to return the book.\n");
    }
    fclose(fp);

}
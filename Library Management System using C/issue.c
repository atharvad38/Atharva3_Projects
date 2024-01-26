#include<stdio.h>
#include<string.h>
#include"issued.c"
extern void issued(char *ptr);
extern void issue(){
    char ch,bug[4],word[12],str[10000],*tmp;
    int i;
    FILE *fp;
    fp = fopen("studentrecord.txt","r");
    gets(bug);
    printf("Enter your Id :");
    gets(word);
    i=0;
    do{
        ch=fgetc(fp);
        str[i]=ch;
        i++;
    }while(str[i]!='\n');
    tmp = strstr(str,word);
    if(tmp!=NULL){
        printf("You are eligible to issue book");
        issued(word);
    }
    else{
        printf("You are not eligible and register yourself to gets books");
    }
    fclose(fp);
}
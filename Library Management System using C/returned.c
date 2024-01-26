#include<stdio.h>
#include<string.h>
extern void returned(char *ptr){
     int l,i,j,id,ch1,ch2;
    char erp[12],str[10000],word[10],*tmp,ch;
    FILE *fp,*fp1,*fp2;
    strcpy(erp,ptr);
    puts(erp);
    l=strlen(erp);
    fp=fopen("bookissuedto.txt","r");
    while((ch=getc(fp))!=EOF){
        printf("c",ch);
    }
    fclose(fp);
    printf("Enter your book id :");
    scanf("%d",&id);
    fp1=fopen("bookissuedto.txt","r");
    do{
    i=0;
    itoa(id,word,10);
    do{
        ch1=fgetc(fp1);
        str[i]=ch1;
        i++;
    }while(str[i]!='\n');
    tmp = strstr(str,word);
    if(tmp!=NULL){
        printf("Your book is returned.\n");
        

    }
    else{
        printf("Your book id is not valid");}
    
        printf("\nIf you want to return more books then enter book id otherwise enter 0 :");

        scanf("%d",&id);
    }while(id!=0);
    fclose(fp);

    
}

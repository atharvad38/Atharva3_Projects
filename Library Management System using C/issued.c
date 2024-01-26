#include<stdio.h>
#include<string.h>
extern void issued(char *ptr){
    int l,i,j,id,ch1,ch2;
    char erp[12],str[10000],word[10],*tmp,ch;
    FILE *fp,*fp1,*fp2;
    strcpy(erp,ptr);
    puts(erp);
    l=strlen(erp);
    fp=fopen("bookrecord.txt","r");
    while((ch=getc(fp))!=EOF){
        printf("c",ch);
    }
    fclose(fp);
    printf("Enter your book id :");
    scanf("%d",&id);
    fp1=fopen("bookrecord.txt","r");
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
        printf("Your book id is  valid\n");
        fp2=fopen("bookissuedto.txt","a");
        fprintf(fp2,"\n%s\t",erp);
        fprintf(fp2,"\n%s\t",word);
        fclose(fp2);
        printf("Issued successfully");

    }
    else{
        printf("Your book id is not valid");
        printf("\nEnter your book id :");
        scanf("%d",&id);
    }}while(id!=0);
    fclose(fp);

    
}
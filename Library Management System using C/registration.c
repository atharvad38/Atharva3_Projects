#include<stdio.h>
#include<string.h>
extern void registration(){
    int n,a;
    //printf("You are in Registration ");
    struct student{
        char name[30];
        char no[15];
        char email[50];
        char dept[20];
        int sem;
        char bug[4];
        char erp[15];
    };
    struct student st;
    FILE *fp;
    fp = fopen("studentrecord.txt","a");
    if(fp==NULL){
        printf("Something went wrong !\n");
        goto end;
    }
    printf("Enter no. of student :");
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        gets(st.bug);
        printf("\nEnter name of Student :");
        gets(st.name);
        fprintf(fp,"\n%s\t",st.name);
        printf("Enter Mobile number of Student :");
        gets(st.no);
        fprintf(fp,"%s\t",st.no);
        printf("Enter department of Student :");
        gets(st.dept);
        fprintf(fp,"%s\t",st.dept);
        printf("Enter email of Student :");
        gets(st.email);
        fprintf(fp,"%s\t",st.email);
        printf("Enter semester of Student :");
        scanf("%d",&st.sem);
        fprintf(fp,"\t%d\t",st.sem);
        srand(time(0));
        a =rand();
        itoa(a,st.erp,10);
        strcat(st.dept,st.erp);
        fprintf(fp,"%s",st.dept);
        printf("\nStudent %d detail is saved.",i+1);
    }
    if(fp==NULL){
        end:
        printf("You have exit from program due to some file issues\n");

    }
    fclose(fp);

}
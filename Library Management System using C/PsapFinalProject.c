#include"registration.c"10
#include"issue.c"
#include"Return.c"
#include"addnew.c"

extern void registration();
extern void issue();
extern void Return();
extern void addnew();



void main(){
    int select;
    do{
    printf("Select Your operation :\n");
    printf("Press 1 for new registration of student\n");
    printf("Press 2 to issue book\n");
    printf("Press 3 to return book\n");
    printf("Press 4 to add new books\n");
    printf("Press 0 for EXIT\n");
    scanf("%d",&select);
    switch(select){
        case 1:
        registration();
        printf("\n\n\n");
        break;

        case 2:
        issue();
        printf("\n\n\n");
        break;

        case 3:
        Return();
        printf("\n\n\n");
        break;

        case 4:
        addnew();
        printf("\n\n\n");
        break;

        default:
        printf("Please Enter a valid option");
        break;
    }
    }while(select!=0);
    printf("You have EXIT from Program");


}
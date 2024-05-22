#include<stdio.h>
#include<stdlib.h>
#include<limits.h>

struct node{
    int dest;
    int weight;
    struct node* next;
};

void AddEdge(struct node* adjlist[],int src,int dest,int weight){
    struct node* newNode = (struct node*)malloc(sizeof(struct node));
    newNode->dest = dest;
    newNode->weight = weight;
    newNode->next = adjlist[src];
    adjlist[src] = newNode;

    
}


void dijkstra(struct node* adjlist[],int vertices,int start,int end){
    int dist[vertices];
    int prev[vertices];
    int visited[vertices] ;
    
    for(int i=0;i<vertices;i++){
        dist[i] = INT_MAX;
        prev[i] =-1;
        visited[i] =0;
    }
    dist[start]  =0;

    for(int count=0;count<vertices-1;count++){
        int mindist =INT_MAX;
        int minindex = -1;
        for(int v=0;v<vertices;v++){
            if(!visited[v]&&dist[v]<mindist){
                mindist = dist[v];
                minindex = v;
            }
        }

        if(minindex==-1){
            break;
        }
        visited[minindex] = 1;
        struct node* node = adjlist[minindex];
        while(node!=NULL){
            int dest = node->dest;
            if(!visited[dest] && dist[minindex]!=INT_MAX && dist[minindex]+node->weight <dist[dest]){
                dist[dest] = dist[minindex] + node->weight;
                prev[dest] = minindex;
            }
            node=node->next;
        }
    }

    if(dist[end]==INT_MAX){
        printf("There exists no path between given source and destination");
        return;

    }
    else{
        int path[vertices];
        int count=0;
        for(int at=end;at!=-1;at = prev[at]){
            path[count++] = at;
        }
        printf("\nThe path between given source and destination is:");
        for(int i=count-1;i>=0;i--){
            printf("%d ",path[i]);
        }
        printf("\nThe shortest distance between given source and destination is : %d",dist[end]);
    }
}

void clearGraph(struct node* adjlist[], int vertices) {
    for (int i = 0; i < vertices; i++) {
        struct node* node = adjlist[i];
        while (node != NULL) {
            struct node* temp = node;
            node = node->next;
            free(temp);
        }
        adjlist[i] = NULL;
    }
}


int main(){
    int vertices;
    printf("Enter the number of vertices : ");
    scanf("%d",&vertices);
    struct node* adjlist[vertices];
    for(int i=0;i<vertices;i++){
        adjlist[i] = NULL;
    }
    int choice = 0;
    int u,v,w;
    while(choice!=4){
        printf("\n1.Add edge\n2.Find Shortest Path\n3.Clear graph\n4.EXIT");
        printf("\nChoose any option from above:");
        scanf("%d",&choice);
        switch(choice){
            case 1:
            printf("Enter the source , destination and weight of edge (u v w):");
            scanf("%d %d %d",&u,&v,&w);
            AddEdge(adjlist,u,v,w);
            break;

            case 2:
            printf("\nEnter the source :");
            scanf("%d",&u);
            printf("\nEnter the destination :");
            scanf("%d",&v);
            dijkstra(adjlist,vertices,u,v);
            break;

            case 3:
            clearGraph(adjlist,vertices);
            printf("\nGraph Cleared!!!!!!");
            break;

            case 4:
            printf("\nBYE BYE.............");
            break;



        }
    }

}

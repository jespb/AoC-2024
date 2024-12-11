#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>



#define MAX_LEN 10000

typedef struct Entry {
    long long key;
    long long value;
} Entry;

long long keyExists(Entry* dic, long long key){
    for(long long i = 0; dic[i].key != -1; i++){
        if (dic[i].key == key){
            return 1;
        }
    }
    return 0;
}

long long newEntry(Entry* dic, long long key, long long v){
    long long i = 0;
    for(i = 0; dic[i].key != -1; i++){}
    dic[i].key = key;
    dic[i].value = v;
    return 0;
}

long long increment(Entry* dic, long long key, long long v){
    for(long long i = 0; dic[i].key != -1; i++){
        if (dic[i].key == key){
            dic[i].value += v;
            return 1;
        }
    }
    return 0;
}

void blink(long long** line){
    Entry *dic = malloc(sizeof(Entry) * MAX_LEN);
    for(long long i = 0; i<MAX_LEN; i++){
        dic[i].key=-1;
    }

    for(long long i = 0; line[i][0]!=-1; i++){
        long long v = line[i][0];
        if (keyExists(dic, v)){
            increment(dic, v, line[i][1]);
        }else{
            newEntry(dic, v, line[i][1]);
        }
    }

    long long** stones = malloc(sizeof(long long)*MAX_LEN);
    for (long long j = 0; j < MAX_LEN; j++){
        stones[j] = malloc(sizeof(long long)*2);
    }

    long long i = 0;
    while (dic[i].key!=-1){
        long long v = dic[i].key;
        long long w = dic[i].value;
        stones[i][0] = v;
        stones[i][1] = w;
        i++; 
    }
    stones[i][0] = -1;

    i = 0;
    long long j = 0;
    while (stones[i][0] != -1){
        long long v = stones[i][0]; 
        if (v == 0){
            line[j][0] = 1;
            line[j][1] = stones[i][1];
            j++;
            i++;
        }else if( (long long)( log(v)/log(10))%2!=0  ){
            long long l = (long long)( log(v)/ log(10))+1;
            line[j][0] = v/pow(10,l/2);
            line[j][1] = stones[i][1];
            j++;
            line[j][0] = v % (long long)(pow(10,l/2));
            line[j][1] = stones[i][1];
            j++;
            i++;
        }else{
            line[j][0] = v*2024;
            line[j][1] = stones[i][1];
            j++;
            i++;
        }
    }
    line[j][0]=-1;

    free(dic);

}

int main(){
    FILE *file;
    char* filename = "input2.txt";
    char line[MAX_LEN];
    long long** stones = malloc(sizeof(long long)*MAX_LEN);
    for (long long j = 0; j < MAX_LEN; j++){
        stones[j] = malloc(sizeof(long long)*2);
    }
    file = fopen(filename, "r");

    fgets(line, sizeof(line), file);

    fclose(file); // Close the file after reading

    // Split the line long longo tokens and convert to long longegers
    char *token = strtok(line, " ");
    int i = 0;
    while (token != NULL) {
        int number = atoi(token); // Convert the token to an long longeger
        stones[i][0] = number;
        stones[i][1] = 1;
        i++;
        token = strtok(NULL, " "); // Get the next token
    }
    stones[i][0] = -1;

    for (int j = 0; j < 75; j++){
        blink(stones);
    }

    long long acc = 0;
    for (long long j = 0; j < MAX_LEN && stones[j][0]!=-1; j++){
        acc += stones[j][1];
    }

    printf("%lld\n", acc);

}


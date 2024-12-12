#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_LEN 7000

int length_int(long v){
    v /= 10;
    int l = 1;
    while (v!=0){
        v /= 10;
        l += 1;
    }    
    return l;
}

int power10(int n){
    int a = 1;
    for (int i = 0; i < n; i++){
        a *= 10;
    }
    return a;
}

long keyExists(long* dic, long key){
    for(int i = 0; dic[i*2] != -1; i++){
        if (dic[i*2] == key){
            return 1;
        }
    }
    return 0;
}

int newEntry(long* dic, long key, long v){
    int i = 0;
    for(i = 0; dic[i*2] != -1; i++){}
    dic[i*2] = key;
    dic[i*2+1] = v;
    return 0;
}

int increment(long* dic, long key, long v){
    for(int i = 0; dic[i*2] != -1; i++){
        if (dic[i*2] == key){
            dic[i*2+1] += v;
            return 1;
        }
    }
    return 0;
}

void blink(long** line, long** stones){
    long* dic = malloc(sizeof(long) *  MAX_LEN*2);

    for(int i = 0; i<MAX_LEN; i++){
        dic[i*2]=-1;
    }

    for(int i = 0; line[i][0]!=-1; i++){
        long v = line[i][0];
        if (keyExists(dic, v)){
            increment(dic, v, line[i][1]);
        }else{
            newEntry(dic, v, line[i][1]);
        }
    }


    int i = 0, j = 0;
    while (dic[i*2] != -1){
        stones[i][0] = dic[i*2];
        stones[i][1] = dic[i*2+1];
        i++; 
    }
    stones[i][0] = -1;

    i = 0, j = 0;
    while (stones[i][0] != -1){
        long v = stones[i][0]; 
        if (v == 0){
            line[j][0] = 1;
            line[j][1] = stones[i][1];
        }else if( length_int(v)%2==0  ){
            int l = length_int(v);
            int p10 = power10(l/2);
            line[j][0] = v/p10;
            line[j][1] = stones[i][1];
            j++;
            line[j][0] = v % p10;
            line[j][1] = stones[i][1];
        }else{
            line[j][0] = v*2024;
            line[j][1] = stones[i][1];

        }
        j++;
        i++;
    }
    line[j][0]=-1;

    free(dic);

}

int main(){
    FILE *file;
    char* filename = "input2.txt";
    char line[MAX_LEN];
    long** stones = malloc(sizeof(long)*MAX_LEN);
    long** trash = malloc(sizeof(long)*MAX_LEN);
    for (long j = 0; j < MAX_LEN; j++){
        stones[j] = malloc(sizeof(long)*2);
        trash[j] = malloc(sizeof(long)*2);
    }
    file = fopen(filename, "r");

    fgets(line, sizeof(line), file);

    fclose(file); // Close the file after reading

    // Split the line longo tokens and convert to longegers
    char *token = strtok(line, " ");
    int i = 0;
    while (token != NULL) {
        int number = atoi(token); // Convert the token to an longeger
        stones[i][0] = number;
        stones[i][1] = 1;
        i++;
        token = strtok(NULL, " "); // Get the next token
    }
    stones[i][0] = -1;


    clock_t begin = clock();
    for (int j = 0; j < 75; j++){
        blink(stones, trash);
    }
    clock_t end = clock();
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;

    long acc = 0;
    for (long j = 0; j < MAX_LEN && stones[j][0]!=-1; j++){
        acc += stones[j][1];
    }

    printf("Took %.5f seconds to calculate: %ld\n", time_spent, acc);

}


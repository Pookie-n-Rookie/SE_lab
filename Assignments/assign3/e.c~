#include <stdio.h>
#include <stdlib.h>
enum states {
    START,
    LOOP,
    END,
} state;

enum events {
    START_LOOPING,
    PRINT_HELLO,
    STOP_LOOPING,
};
void step_state(enum events event) {
    switch(state) {
    case START:
        switch(event) {
        case START_LOOPING:
            state = LOOP;
            break;
        default:
            exit(1);
            break;
        }       
        break;
    case LOOP:
        switch(event) {
        case PRINT_HELLO:
            printf("Hello World!\n");
            break;
        case STOP_LOOPING:
            state = END;
            break;
        default:
            exit(1);
            break;
        }
        break;
    case END:
        exit(1);
        break;
    }
}
int main(void) {
    int cntr =0 ;
    events events_arr[] = { START_LOOPING, PRINT_HELLO, PRINT_HELLO, PRINT_HELLO, PRINT_HELLO, PRINT_HELLO,PRINT_HELLO,PRINT_HELLO,STOP_LOOPING,PRINT_HELLO,PRINT_HELLO,STOP_LOOPING};
    while(events_arr[cntr] != STOP_LOOPING)
    {
        step_state(events_arr[cntr]);
        cntr++;
    }
   
    if (cntr == 10) {
        printf("PASS");
    } else {
        printf("FAIL %d", cntr);
    }
    
    return 0;
}

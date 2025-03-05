/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
C#, VB, Perl, Swift, Prolog, Javascript, Pascal, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdlib.h>
enum states {
    START,
    LOOP,
    END,
} state;

enum events {
    START_LOOPING,
    USERID_MATCHED,
    SHOW_DETAIL,
    STOP_LOOPING,
};
 
int valid_id(int id)
{
	if ( id > 0 && id < 20)
		return 1;
	else
		return 0;
}

int valid_pw(int id, int password)
{
	
	if (password == id*1000)
		return 1;
	return 0;
}
int show(int id)
{
    return id*100000;
}
void step_state(enum events event) {
    int cntr= 0;
while(1) {
	    int id , password;
	    cntr++;
    switch(state) {
    case START:
        switch(event) {
        case START_LOOPING:
	{
            state = LOOP;
            if (cntr > 10) {
                printf("Session expired!");
                event = STOP_LOOPING;
                state = END;
	        } else {
                printf("Hello Please Provide  User Id and Password to see your details!\n");
	            printf("User Id: ");
	            scanf("%d", &id);
	            if (valid_id(id)) {
		            event = USERID_MATCHED ;
	            } else {
		            printf("Incorrect User Id!!");
		            event = START_LOOPING ;
		            state = START ;
	            }
	        }
	        
            break;
	}
	case STOP_LOOPING:
	{
	    printf("Invaid state\n");
	    break;
	}
        default:
            exit(1);
            break;
        }       
        break;
    case LOOP:
        switch(event) {
        case USERID_MATCHED:
	    printf("Password: ");
	    scanf("%d", &password);
	    if (valid_pw(id,password)) {
		    event = SHOW_DETAIL ;
	    } else {
		    printf("Incorrect password!!\n");
		    event = STOP_LOOPING ;
		    state = END;
	    }
            break;
        case SHOW_DETAIL:
	   {
		   char c = 'p';
	    printf("User Id : %d, Password: %d , Amount : %d\n", id,password,show(id));
	    state = START ;
	    event = START_LOOPING; 
	    
	    }
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
}
int main(void) {
    step_state(START_LOOPING);
   
    return 0;
}


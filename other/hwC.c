// hw from book

// 1.8. 
#include <stdio.h>

int main() {
    int i;
    int tab = 0;
    while ((i = getchar()) != EOF) {
        if (i == '\t')  // or ' ' or '\n'
            tab++;
        i++;
    }
    printf("Tab: %d\n", tab);
}

//1.9
#include <stdio.h>

int main() {
 
    int i, j; 
    j = 0;
    while ((i = getchar()) != EOF) {
        if (i == ' ' && j == 0) {
            putchar(i);
            ++j;
        }
        if (i == ' ' && j != 0) {
            ++j;
        }
        if (i != ' ') {
            putchar(i);
            j = 0;
        }
    } 
}

//1.10
#include <stdio.h>

int main() {
	int i;
	while ((i = getchar()) != EOF) {
		if (i == '\t') {
			putchar('\\');
			putchar('t');
		}
		else if (i == '\b') {
			putchar('\\');
			putchar('b');
		} else if (i == '\\') {
			putchar('\\');
		}
		putchar(i);
	}
}

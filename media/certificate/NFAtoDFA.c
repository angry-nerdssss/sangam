#include <stdio.h> // for I/O (printf/ scanf)
#define N 1000     // just an assumption as to how many states can possibly be formed in DFA

typedef struct Stack { // structure for stack
	int a[N], top;
} STACK;
int isEmpty(STACK *s) { // to check whether stack in empty
	return s->top == -1;
}
void push(STACK *s, int item) { // to push element to top of stack
	s->a[++s->top] = item;
}
int pop(STACK *s) { // to get the top most element in stack
	return s->a[s->top--];
}

void printList(int n, int r, int a[][r + 1][n + 1]) { // to display the machine (NFA) taken as input
	int i, j, k;
	for (i = 0; i < n; i++) {     // iterating over states
		for (j = 0; j < r; j++) { // iterating over input symbols
			int count = a[i][j][0];
			for (k = 1; k <= count; k++)
				printf("From %d to %d by %d\n", i, a[i][j][k], j);
		}
		int count = a[i][r][0];
		for (k = 1; k <= count; k++)
			printf("From %d to %d by epsilon\n", i, a[i][r][k]);
	}
}

void bubbleSort(int a[], int n) { // used here to sort array before removing duplicates
	int i, j, temp;
	for (i = 1; i <= n - 1; i++) {
		for (j = 1; j <= n - i - 1; j++)
			if (a[j] > a[j + 1]) {
				temp = a[j];
				a[j] = a[j + 1];
				a[j + 1] = temp;
			}
	}
}

void printStates(int arr[][N + 1], int nos) { // to print state containing array
	int i, j;
	for (i = 0; i < nos; i++) {
		printf("State %d consists of: ", i);
		for (j = 1; j <= arr[i][0]; j++) {
			printf("%d, ", arr[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}

void removeDuplicates(int arr[]) { // to remove duplicate elements (here states) from an array
	int n = arr[0];
	bubbleSort(arr, n); // sort the array
	if (n == 0 || n == 1)
		return;
	int i, j = 0;
	for (i = 1; i <= n - 1; i++)
		if (arr[i] != arr[i + 1]) // check unique
			arr[++j] = arr[i];
	arr[++j] = arr[n];
	arr[0] = j;
}

int contains(int states[][N + 1], int a[], int nos) { // to check whether the state newly made already exists in DFA
	int i, j;
	for (i = 0; i < nos; i++) {
		// printf("Compare\n");
		// printStates(states[i]);
		// printStates(a);
		if (states[i][0] == a[0]) { // check same number of elements in set
			for (j = 1; j <= a[0]; j++)
				if (states[i][j] != a[j])
					break;
			if (j > a[0]) {
				// printf("Success %d\n", i);
				return i;
			}
		}
	}
	return -1;
}

void printClosure(int n, int clo[][n]) { // to print the closure of all states in NFA
	int i, j;
	for (i = 0; i < n; i++) { // iterating over states
		printf("Closure of %d: ", i);
		for (j = 0; j < n; j++)
			if (clo[i][j])
				printf("%d ", j);
		printf("\n");
	}
}

void printTable(int nos, int r, int table[][r]) { // to print the DFA's transition table made
	int i, j;
	for (i = 0; i < nos; i++)
		for (j = 0; j < r; j++)
			printf("From state %d with input %d goes to %d\n", i, j, table[i][j]);
}

int checkFinal(int a[], int final[]) { // to check whether state is final or not
	int i;
	for (i = 1; i <= a[0]; i++)
		if (final[a[i]])
			return 1;
	return 0;
}

int main() { // the main method
	printf("Enter number of states: ");
	int n, r, i, j, k, l, temp, state;
	char dummy;
	scanf("%d", &n); // taking input number of states
	printf("Enter number of input characters: ");
	scanf("%d", &r); // taking input number of input characters
	int a[n][r + 1][n + 1];
	for (i = 0; i < n; i++) { // taking input over all states (all statesment are self descriptive)
		for (j = 0; j < r; j++) {
			printf("Enter number of states from state %d with input %d: ", i, j);
			scanf("%d", &temp);
			a[i][j][0] = temp;
			if (temp != 0)
				printf("Enter %d states: ", temp);
			for (k = 1; k <= temp; k++) {
				scanf("%d", &state);
				a[i][j][k] = state;
			}
		}
		printf("Enter number of states from state %d with epsilon moves: ", i); // still taking input
		scanf("%c%d", &dummy, &temp);
		a[i][r][0] = temp;
		if (temp != 0)
			printf("Enter %d states:\n", temp);
		for (k = 1; k <= temp; k++) {
			scanf("%d", &temp);
			a[i][r][k] = temp;
		}
	}
	// printList(n, r, a);

	int clo[n][n]; // closure
	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++)
			clo[i][j] = 0;
	for (i = 0; i < n; i++) { // making closure for all
		STACK s;
		s.top = -1;
		push(&s, i); // pushing to stack s
		clo[i][i] = 1;
		while (!isEmpty(&s)) {
			int this = pop(&s);
			for (j = 1; j <= a[this][r][0]; j++)
				if (!clo[i][a[this][r][j]]) {
					push(&s, a[this][r][j]);
					clo[i][a[this][r][j]] = 1;
				}
		}
	}
	// printClosure(n, clo);

	int nf, final[N];
	printf("Enter number of final states:\n");
	scanf("%c%d", &dummy, &nf);
	printf("Enter final states:\n");
	for (i = 0; i < n + 5; i++)
		final[i] = 0; // initialising with 0
	for (i = 0; i < nf; i++) {
		scanf("%d", &temp); // taking input of final states
		final[temp] = 1;    // initialising with 1
	}

	int states[N][N + 1], nos = 1, table[N][r];
	for (i = 0; i < N; i++) // initialising with 0
		states[i][0] = 0;
	for (i = 0; i < n; i++)
		if (clo[0][i]) // creating first state
			states[0][++states[0][0]] = i;
	removeDuplicates(states[0]);  // removing duplicate state entries
	for (i = 0; i < nos; i++) {   //for every state
		for (j = 0; j < r; j++) { // for every input symbol
			int b[N];
			b[0] = 0;
			for (k = 1; k <= states[i][0]; k++)
				for (l = 1; l <= a[states[i][k]][j][0]; l++) { // creating state list using closure list
					int st = a[states[i][k]][j][l], ii;
					for (ii = 0; ii < n; ii++)
						if (clo[st][ii])
							b[++b[0]] = ii;
				}
			if (b[0] == 0) { // is no destination state found
				b[0] = 1;
				b[1] = i;
			}

			removeDuplicates(b); // removing duplicate state entries
			int con = contains(states, b, nos);
			if (con == -1) {
				states[nos][0] = b[0];
				for (k = 1; k <= b[0]; k++)
					states[nos][k] = b[k];
				table[i][j] = nos;
				// printf("Added: %d %d %d\n", i, j, nos);
				nos++;
			} else {
				table[i][j] = con;
				// printf("Added: %d %d %d\n", i, j, con);
			}
		}
	}
	printf("\n------------DFA--------------\n");
	printf("\nNumber of states: %d, Number of input symbols: %d, Initial state is 0\n", nos, r);
	printTable(nos, r, table);
	printf("\nThe DFA states consist of following NFA states:\n");
	printStates(states, nos);
	printf("\n");
	printf("Final states are: ");
	for (i = 0; i < nos; i++)
		if (checkFinal(states[i], final))
			printf("%d, ", i);
	printf("\n");
	return 0;
}

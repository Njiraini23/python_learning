#include <stdio.h>

int main(int argc, char **argv)
{
	int i;
	while (*argv != NULL)
		printf("%s\n",*argv), argv++;

	for (i = 0; argv[i] != NULL; i++)
		printf("%s\n", *argv);
	return (0);
}

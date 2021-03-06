#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
/**
 * infinite_while - infinite loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - creates 5 zombie processes
 * Return: 0
 */
int main(void)
{
	int x;
	pid_t z_pid;

	for (x = 0; x < 5; x++)
	{
		z_pid = fork();
		if (z_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", z_pid);
		}
		else
			exit(0);
	}
	infinite_while();
	return (0);
}

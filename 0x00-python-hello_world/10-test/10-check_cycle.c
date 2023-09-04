#include <stdio.h>
#include "lists.h"
int check_cycle(listint_t *list)
{
	listint_t *current, **adrs = NULL;
	int n = 0,x, c;


	current = malloc(sizeof(listint_t));
	if (!current)
		return (-1);
	current = list;
	while (current->next)
	{
		current = current->next;
		n++;
	}
	current = list;
	c = 0;
	while (current)
	{
		for (x = 0; x < c; x++)
		{
			if (current->next == adrs[x])
				return (1);
		}
		adrs[c] = current;
		current = current->next;
		c++;
	}
	free(current);
	return (0);
}

#include <stdio.h>
/**
 * is_palindrome - checks if a single linked list is a palindrom
 * @head: the head of the list to be checked
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int len, x, c;
	listint_t tmp1, tmp2, current;

	if (!head || !head->next || !(head->next)->next)
		return (1);
	len = 0;
	current = head;
	while (current->next)
	{
		len++;
		current = current->next
	}
	while (len / 2)
	{
		for (int i = 0; i < len; i++)
			tmp1 = head->next;
		if (tmp1->n == tmp2->n)
			continue
		x = head->n;

	}
}

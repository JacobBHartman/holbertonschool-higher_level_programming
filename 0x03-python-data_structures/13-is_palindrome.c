#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: a pointer to a pointer to a singly linked list
 * Return: 0 if not a palindrome, 1 if is a palindrome
 */
int is_palindrome(listint_t **head)
{
	/* declare variables */
	listint_t *top = *head;
	listint_t *bot = *head;
	listint_t *crumb = *head;

	/* check if head is null */
	if (head == NULL)
		return (0);

	if (*head == NULL)
		return (0);

	/* initialize the positions of the bot pointer and crumb */
	while (bot->next != NULL)
	{
		if (bot->next->next == NULL)
			crumb = bot;
		bot = bot->next;
	}

	/* primary functionality */
	while (bot != top && bot->next != top)
	{
		if (bot->n != top->n)
			return (0);
		bot = crumb;
		top = top->next;
		crumb = top;
		while (crumb->next != bot && bot->next != crumb)
			crumb = crumb->next;
	}
	return (1);

}

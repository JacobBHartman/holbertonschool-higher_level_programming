#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: a pointer to a list (i.e. the head)
 *
 * Return: 1 if it's a cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *checker;
	listint_t *breadcrumb;

	checker = list;
	breadcrumb = list;
	while (checker != NULL && checker->next != NULL)
	{
		checker = (checker->next)->next;
		breadcrumb = breadcrumb->next;
		if (checker == breadcrumb)
			return (1);
	}
	return (0);
}

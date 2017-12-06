#include "lists.h"

/**
 * insert_node - inserts a number into a sorted signly linked list
 * @head: a pointer to a pointer to a list
 * @number: the number to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *new_node;
	listint_t *breadcrumb;

	/* check if head(s) is null */
	if (head == NULL)
		return (NULL);

	/* create a new node and assign it values, check if fails */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (*head);
	}
	else
	{
		while (new_node->n >= temp->next->n)
			temp = temp->next;
		breadcrumb = temp;
		temp = temp->next;
		breadcrumb->next = new_node;
		breadcrumb->next->next = temp;
	}
	return(breadcrumb->next);
}

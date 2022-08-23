#include "lists.h"
/**
 * insert_node - The function inserts a new node into a sorted linked
 * list
 * @head: Pointer to the address of the head node...
 * @number: The new number
 * Return: The address of the new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = NULL;
	listint_t *new = NULL;
	listint_t *old = NULL;

	if (*head == NULL)
	{
		*head = malloc(sizeof(listint_t));
		if (*head == NULL)
			return (NULL);
		(*head)->n = number;
		(*head)->next = NULL;
		return (*head);
	}
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	ptr = *head;
	while (ptr)
	{
		if (ptr->n > number)
		{
			new->n = number;
			new->next = ptr;
			if (old)
				old->next = new;
			else
				*head = new;
			return (new);
		}
		old = ptr;
		ptr = ptr->next;
	}
	new->n = number;
	new->next = NULL;
	old->next = new;
	return (new);
}

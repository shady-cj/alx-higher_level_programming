#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Checks if there is cycle in a singly linked list
 * @list: The address to the head node of the linked list
 * Return: 0 if there is no cycle 1 if there's cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *hare = NULL;
	listint_t *tortoise = NULL;
	if (list == NULL || list->next == NULL)
		return (0);

	hare = list->next->next;
	tortoise = list;
	while (hare != NULL)
	{
		if (hare == tortoise)
		{
			return (1);
		}
		tortoise = tortoise->next;
		if (hare->next != NULL)
			hare = hare->next->next;
		else
			hare = hare->next;
	}
	return (0);
}

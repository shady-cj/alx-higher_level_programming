#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - function in C that checks if a singly linked
 * list is a palindrome
 * @head: The address to the head node
 * Return: 1 if the list is a palindrome and 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *new_head = NULL;
	listint_t *ptr_1 = NULL;
	listint_t *ptr_2 = NULL;

	if (*head == NULL)
		return (1);
	duplicate_linked_list(&new_head, *head);
	ptr_1 = *head;
	ptr_2 = new_head;

	while (ptr_1 != NULL && ptr_2 != NULL)
	{
		if (ptr_1->n != ptr_2->n)
			return (0);
		ptr_1 = ptr_1->next;
		ptr_2 = ptr_2->next;
	}
	free_listint(new_head);
	if (ptr_1 == NULL && ptr_2 == NULL)
		return (1);
	else
		return (0);
}

/**
 * duplicate_linked_list - Duplicates the linked list in reverse.
 * @new_head: The address to the new head node
 * @head: The main head node
 * Return: void
 */

void duplicate_linked_list(listint_t **new_head, listint_t *head)
{
	listint_t *ptr = NULL;
	listint_t *new = NULL;
	listint_t *current = NULL;

	current = head;
	ptr = malloc(sizeof(listint_t));
	if (ptr == NULL)
		return;
	ptr->n = current->n;
	ptr->next = NULL;
	current = current->next;
	while (current != NULL)
	{
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return;
		new->n = current->n;
		new->next = ptr;
		ptr = new;
		current = current->next;
	}
	*new_head = ptr;
}

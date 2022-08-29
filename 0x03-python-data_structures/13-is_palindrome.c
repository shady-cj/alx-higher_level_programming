#include <stdio.h>
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
	reverse_duplicate(&new_head,
                new_head, NULL, NULL
                );
	ptr_1 = *head;
	ptr_2 = new_head;

	while (ptr_1 != NULL && ptr_2 != NULL)
	{
		if (ptr_1->n != ptr_2->n)
			return (0);
		ptr_1 = ptr_1->next;
		ptr_2 = ptr_2->next;
	}
	if (new_head != NULL)
		free_listint(new_head);
	if (ptr_1 == NULL && ptr_2 == NULL)
		return (1);
	else
		return (0);
}

/**
 * duplicate_linked_list - Duplicates the linked list..
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
	*new_head = malloc(sizeof(listint_t));
	if (*new_head == NULL)
		return;
	(*new_head)->n = current->n;
	(*new_head)->next = NULL;
	ptr = *new_head;
	current = current->next;
	while (current != NULL)
	{
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return;
		new->n = current->n;
		new->next = NULL;
		ptr->next = new;
		ptr = ptr->next;
		current = current->next;
	}
}

/**
 * reverse_duplicate - This reverses the initially duplicated linked list.
 * @new_head: Address to the new duplicated head node to be reversed
 * Return: void
 */

void reverse_duplicate(listint_t **new_head,
		listint_t *current, listint_t *prev,
		listint_t *next
		)
{
	if (current == NULL)
	{
		*new_head = prev;
		return;
	}
	next = current->next;
	current->next = prev;
	prev = current;
	current = next;
	reverse_duplicate(new_head,
                current, prev, next
                );
}

#include <stdlib.h>
#include <stdio.h>
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
	int is_palindrome;

	if (*head == NULL)
		return (1);
	duplicate_linked_list(&new_head, *head);
	ptr_1 = *head;
	ptr_2 = new_head;

	is_palindrome = compare_lists(ptr_1, ptr_2);
	free_listint(new_head);
	return (is_palindrome);
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

/**
 * compare_lists - This function compares the 2 lists.. the main list and
 * the reversed list recursively
 * @reversed_head: The head node to the reversed list
 * @head: The head node to the main list
 * Return: 1 if palindromic and 0 if not
 */

int compare_lists(listint_t *head, listint_t *reversed_head)
{
	if (head == NULL || reversed_head == NULL)
		return (1);
	if (head->n != reversed_head->n)
		return (0);
	return (compare_lists(head->next, reversed_head->next));
}

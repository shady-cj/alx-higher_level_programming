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
	listint_t *ptr_right = NULL;
	listint_t *ptr_left = NULL;

	if (*head == NULL)
		return (1);
	ptr_left = *head;
	ptr_right = *head;
	return (compare_rec(&ptr_left, ptr_right));
}

/**
 * compare_rec - This function compares the 2 lists recursively.
 * @right_ptr: The head node which moves to the right during the
 * recursive call.
 * @left_ptr: The address of the pointer to the main head node.
 * Return: 1 if palindromic and 0 if not
 */

int compare_rec(listint_t **left_ptr, listint_t *right_ptr)
{
	int ret, cmp;
	if (right_ptr == NULL)
		return (1);

	ret = compare_rec(left_ptr, right_ptr->next);
	if (ret == 0)
		return (0);
	cmp = (*left_ptr)->n == right_ptr->n;
	*left_ptr = (*left_ptr)->next;
	return (cmp);
}

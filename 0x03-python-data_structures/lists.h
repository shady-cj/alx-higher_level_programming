#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
/* void duplicate_linked_list(listint_t **new_head, listint_t *head); */
size_t duplicate_linked_list(listint_t **new_head, listint_t *head);
/* void reverse_duplicate(listint_t **new_head); */
/*int compare_lists(listint_t *head, listint_t *reversed_head,
		size_t start, size_t end);*/
int compare_rec(listint_t **left_ptr, listint_t *right_ptr);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

#endif /* LISTS_H */

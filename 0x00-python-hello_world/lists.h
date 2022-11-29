#ifndef LISTS_H_
#define LISTS_H_

#include <stdlib.h>

/**
 * struct listint_s - Singly Linked List
 * @n: Integer
 * @next: Points to the next node
 *
 * Description: Singly Linked List node structure
 * for ALX project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
}listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */

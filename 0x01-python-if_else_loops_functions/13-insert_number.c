#include "lists.h"

/**
 * insert_node - Function that Inserts number to a  singly-linked list.
 * @head: Pointer to the head of the linked list.
 * @number: inserted number.
 *
 * Return: NULL if it fails
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new_number;

	new_number = malloc(sizeof(listint_t));
	if (!new_number)
		return (NULL);
	(*new_number).n = number;

	if (!node || node->n >= number)
	{
		new_number->next = node;
		*head = new_number;
		return (new_number);
	}

	while (node && (*node).next && node->next->n < number)
		node = (*node).next;

	(*new_number).next = (*node).next;
	(*node).next = new_number;

	return (new_number);
}

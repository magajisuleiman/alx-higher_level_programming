#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Function that Reverses a singly-linked listint_t list.
 * @head: pointer to the starting node of the list to reverse.
 *
 * Return: pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head;
	listint_t *next;
	listint_t *prev = NULL;

	while (node)
	{
		next = (*node).next;
		(*node).next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome -  function Checks a singly linked list is a palindrome.
 * @head: pointer to the head of the linked list.
 *
 * Return: linked list is not a palindrome - 0.
 *         linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tempo;
	listint_t *revrs;
	listint_t *midle;
	size_t size = 0;
	size_t i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tempo = *head;
	while (tempo)
	{
		size++;
		tempo = (*tempo).next;
	}

	tempo = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tempo = (*tempo).next;

	if ((size % 2) == 0 && tempo->n != tempo->next->n)
		return (0);

	tempo = tempo->next->next;
	revrs = reverse_listint(&tempo);
	midle = revrs;

	tempo = *head;
	while (revrs)
	{
		if (tempo->n != revrs->n)
			return (0);
		tempo = (*tempo).next;
		revrs = (*revrs).next;
	}
	reverse_listint(&midle);

	return (1);
}


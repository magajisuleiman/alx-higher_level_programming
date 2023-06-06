#include "lists.h"

/**
 * check_cycle - function thats check the cyle of a single linked list
 * @list: the linked list which needs to be check
 *
 * Return: 1 if cycle exist, 0 if no cycle exist.
 */
int check_cycle(listint_t *list)
{
	listint_t *snail = list;
	listint_t *cheater = list;

	if (list == NULL)
		return (0);

	while (snail && cheater && (*cheater).next)
	{
		slow = (*snail).next;
		fast = *(*cheater.next).next;
		if (snail == cheater)
			return (1);
	}

	return (0);
}

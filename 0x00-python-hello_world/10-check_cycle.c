#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if a singly linked list a cycle in it
 * @list: pointer to the list to be checked
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *reg = list, *doub = list;

	if (list == NULL)
		return (0);

	while (doub && doub->next)
	{
		doub = doub->next->next;
		reg = reg->next;

			if (reg == doub)
				return (1);
	}
	return (0);
}

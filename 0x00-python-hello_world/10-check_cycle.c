#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
<<<<<<< HEAD
	}

	return (0);
}
=======
	}}
>>>>>>> 4b3cce69550c1dc02fd054135f26bdbeaf8c6a6a

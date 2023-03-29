{
    listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;
    if (*head == NULL || (*head)->next == NULL)
    return (1);

    while (1)
    {
        fast = fast->next->next;
        if (!fast)
        {
            dup = slow->next;
            break;
            }
        if (!fast->next)
        {
            dup = slow->next->next;
            break;
            }
        slow = slow->next;
        }




         

void insert()
{
	int item;

	if (rear == MAX -1)
		printf("Queue Overflow \n");
	else
	{
		if (front == -1)
			front = 0;
		printf("Insert the element in queue : ");
		scanf("%d", &item);
		rear = rear + 1;
		queue_array[rear] = item; 
	}
}

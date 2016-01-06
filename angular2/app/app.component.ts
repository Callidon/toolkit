import {Component} from 'angular2/core';
import {TodoTask} from './todo-task.component';
import {Task} from './task';

@Component({
    selector: 'todo-list',
	directives: [TodoTask],
    template: `
		<ul>
			<li *ngFor='#todo of todos'>
				<todo-task [task]=todo ></todo-task>
			</li>
		</ul>
	`
})
export class TodoList {
	public todos: Task[] = [
		{
			id: 1,
			text: 'Faire les courses'
		},
		{
			id: 2,
			text: 'Sortir le chien'
		}
	];
}

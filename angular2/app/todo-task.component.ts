import {Component} from 'angular2/core';
import {Task} from './task';

@Component({
    selector: 'todo-task',
	inputs: [ 'task' ],
    template: '<span>{{ task.text }}</span>'
})
export class TodoTask {
	public task: Task;
}

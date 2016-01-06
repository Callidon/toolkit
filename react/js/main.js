const React = require('react');
const ReactDOM = require('react-dom');

// Plain old datas
const datas = [
	{
		id: 1,
		author: 'Jean',
		text: 'A comment'
	},
	{
		id: 2,
		author: 'Claude',
		text: 'An other comment'
	}
];

// A container for comments
const CommentBox = React.createClass({
	handleCommentSubmit: function (comment) {
		this.props.data.push(comment);
	},
	render: function () {
		return (
			<div className="commentBox">
				<h1>Comments</h1>
				<CommentList data={this.props.data} />
				<CommentForm onCommentSubmit={this.handleCommentSubmit} />
			</div>
		);
	}
});

const CommentList = React.createClass({
	render: function () {
		const commentNodes = this.props.data.map((comment) => {
			return (
				<Comment author={comment.author} key={comment.id}>
					{ comment.text }
				</Comment>
			);
		});
		return (
			<div className="commentList">
				{ commentNodes }
			</div>
		);
	}
});

const Comment = React.createClass({
	render: function () {
		return (
			<div className="comment">
				<h2>{ this.props.author }</h2>
				<p>{ this.props.children.toString() }</p>
			</div>
		);
	}
});

// A form to add comments
const CommentForm = React.createClass({
	getInitialState: function () {
		return {
			author: '',
			text: ''
		};
	},
	handleAuthorChange: function (e) {
		this.setState({
			author: e.target.value
		});
	},
	handleTextChange: function (e) {
		this.setState({
			text: e.target.value
		});
	},
	handleSubmit: function (e) {
		e.preventDefault();
		const author = this.state.author.trim();
		const text = this.state.text.trim();
		if (!text || !author) {
			return;
		}
		this.props.onCommentSubmit({
			id: Math.random(),
			author: author,
			text: text
		});
	},
	render: function () {
		return (
			<form className="commentForm" onSubmit={this.handleSubmit}>
				<input type="text" placeholder="Your name" value={this.state.author} onChange={this.handleAuthorChange} />
				<input type="text" placeholder="Your comment" value={this.state.text} onChange={this.handleTextChange} />
				<input type="submit" value="Submit" />
			</form>
		);
	}
});

// Render the container in the DOM
ReactDOM.render(
	<CommentBox data={datas} />,
	document.getElementById('container')
);

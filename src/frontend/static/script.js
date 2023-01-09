const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const signUpClick = document.getElementById('signUpClick');
const signInClick = document.getElementById('signInClick');


const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

signUpClick.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInClick.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});
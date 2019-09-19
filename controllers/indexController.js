
const { generateMessageFromKey } = require("../services/messageService")();

const controller = () => {
	const input = document.getElementById("input");

	input.addEventListener("keyup", function(event){
		const { keyCode } = event;
		document.getElementById("age").innerHTML = generateMessageFromKey(keyCode);
	});
}


module.exports = controller;

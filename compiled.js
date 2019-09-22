attachView("../views/input.template.html", "root");
attachView("../views/age.template.html", "root");

const indexController = (function(){
const { generateMessageFromKey } = (function(){const messageService = () => ({
	generateMessageFromKey: (keyCode) => keyCode.toString()
})

return  messageService;})()();

const controller = () => {
	const input = document.getElementById("input");

	input.addEventListener("keyup", function(event){
		const { keyCode } = event;
		document.getElementById("age").innerHTML = generateMessageFromKey(keyCode);
	});
}

//hello world asdasd
return  controller;
})();
indexController();
function require(url){
	if(url.toLowerCase().substr(-3)!=='.js') url+=".js";
	if(!require.cache) require.cache =[];
	let exports = require.cache[url];
	
	if(!exports){
		try{
			exports = {}; 
			const xHttp = new XMLHttpRequest();
			xHttp.open("GET", url, 0);
			xHttp.send();
			if(xHttp.status && xHttp.status === 200){
				const source = xHttp.responseText;
				const module = {id: url, uri:url, exports:exports};
				const anonFn = new Function("require", "exports", "module", source);
				anonFn(require, exports, module);
				require.cache[url] = exports = module.exports;
			}
		} catch (err) {
			console.error(err);
			console.error(`At ${url}`);
		}
	}
	return exports;
}

//console.log("yes")
function attachView(url, docId){
	if(!attachView.cache) attachView.cache =[];
	let data = attachView.cache[url];
	
	if(!data){
		try{
			data = {}; 
			const xHttp = new XMLHttpRequest();
			xHttp.open("GET", url, 0);
			xHttp.send();
			if(xHttp.status && xHttp.status === 200){
				data = xHttp.responseText;
				attachView.cache[url] = data;
			}
		} catch (err) {
			console.error(err);
			console.error(`At ${url}`);
		}
	}
	
	document.getElementById(docId).innerHTML  = document.getElementById(docId).innerHTML  ? document.getElementById(docId).innerHTML + data : data;
	return true; 
}
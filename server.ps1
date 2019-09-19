$http = [System.Net.HttpListener]::new()

$http.Prefixes.Add("http://localhost:8080/")

$http.Start() 




if  ($http.IsListening) {
    Write-Host "HTTP Server Ready! " -f Black -b Green
    Write-Host "now trying to $($http.Prefixes)" -f 'y'
    Write-Host "then try going to $($http.Prefixes)other/path" -f 'y'
}

while ($http.IsListening){
    $context = $http.GetContext()

    if ($context.Request.HttpMethod -eq 'GET' -and $context.Request.RawUrl -eq '/'){
        Write-Host "$($context.Request.UserHostAddress) => $($context.Request.Url)" -f 'mag'
        [string]$html = Get-Content ".\index.html" -Raw 

        $buffer = [System.Text.Encoding]::UTF8.GetBytes($html)
        $context.Response.ContentLength64 = $buffer.Length
        $context.Response.OutputStream.Write($buffer, 0, $buffer.Length)
        $context.Response.OutputStream.Close()
    }

    if ($context.Request.HttpMethod -eq 'GET' -and $context.Request.RawUrl -ne '/'){
        Write-Host "$($context.Request.UserHostAddress) => $($context.Request.Url)" -f 'mag'
        [string]$html = Get-Content ".\$($context.Request.RawUrl)" -Raw 

        $buffer = [System.Text.Encoding]::UTF8.GetBytes($html)
        $context.Response.ContentLength64 = $buffer.Length
        $context.Response.OutputStream.Write($buffer, 0, $buffer.Length)
        $context.Response.OutputStream.Close()
    }
}
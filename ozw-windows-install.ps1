$x=[System.IO.Path]::GetTempFileName(); (new-object net.webclient).DownloadFile("https://gist.githubusercontent.com/ldhertert/6a5597a93013da06044a/raw/install-ozw-windows.js",$x); node $x;
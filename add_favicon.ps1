$directory = "c:\Users\LENOVO\Desktop\art otc"
$faviconTag = "`n    <link rel=`"icon`" type=`"image/png`" href=`"im/X9.png`">"
$files = Get-ChildItem -Path $directory -Filter "*.html"

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw
    
    if ($content -match '<link rel="icon"') {
        Write-Host "Favicon already exists in $($file.Name), skipping."
        continue
    }

    if ($content -match '</title>') {
        $newContent = $content -replace '</title>', ('</title>' + $faviconTag)
        Set-Content -Path $file.FullName -Value $newContent -NoNewline
        Write-Host "Added favicon to $($file.Name)"
    }
    else {
        Write-Host "Could not find </title> tag in $($file.Name)"
    }
}

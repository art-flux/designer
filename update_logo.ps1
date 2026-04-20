$files = Get-ChildItem -Path "c:\Users\LENOVO\Desktop\art otc" -Filter "*.html"
$pattern = '(?s)<div class="container mx-auto .*? flex justify-between items-center">\s*<a href="index.html" class="flex items-center"><img src="im/x8\.png" alt="ART FLUX DESIGNER"\s*class="h-\[\d+px\] w-auto"></a>'
$replacement = '<div class="container mx-auto px-2 py-2 flex justify-between items-center">
            <a href="index.html" class="flex items-center"><img src="im/x8.png" alt="ART FLUX DESIGNER"
                    class="h-[60px] w-auto"></a>'

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw
    if ($content -match $pattern) {
        Write-Host "Updating $($file.Name)..."
        $newContent = $content -replace $pattern, $replacement
        Set-Content -Path $file.FullName -Value $newContent -NoNewline
    }
    else {
        Write-Host "Pattern not found in $($file.Name)"
        # Try a slightly different pattern for files where classes might be ordered differently? 
        # But grep showed they all have im/x8.png.
    }
}

# Get-Content env_example.env | ForEach-Object {
#     if($_){
#         $key, $value = $_.Split('=',2).Trim()        
#         [Environment]::SetEnvironmentVariable($key, $value)
#     }
# }